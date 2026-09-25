
import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient()

llm = init_chat_model(
    model="gemini-3.6-flash",
    model_provider="google_genai",
    api_key=os.environ.get("GOOGLE_API_KEY")
)

@tool
def web_search(query: str) -> dict[str, any]:
    '''Web Search tool for Agent'''
    return tavily_client.search(query)

system_prompt = '''You are a personal chef.

The user will ask you what they can cook with ingredients they have.
Use the web_search tool to search the web for suitable recipes whenever
you need recipe ideas or cooking information.

After searching, provide the user with:
1. The name of the dish.
2. Ingredients required.
3. Step by step cooking instructions.
4. Approximate cooking time.
5. Useful substitutions if appropriate.

Keep the instructions concise but simple and easy to follow.
Keep the final response under 500 words.
If the user mentions ingredients they already have, prioritise recipes
that use those ingredients. Don't use hyphens, em dashes and always use british english.

'''


agent = create_agent(
    model = llm,
    tools = [web_search],
    system_prompt= system_prompt,
)

def main():

    print("1. Starting program...")

    config = {"configurable":{"thread_id":"1" }} 

    while True:

        question = input("State your question: ")

        if question.lower() in ['exit', 'quit']:break

        question_message = HumanMessage(content= question)

        print("2. Calling agent...")

        response = agent.invoke(
            {"messages": [question_message]},
            config
        )

        print("3. Agent responded!")


        final_response = response["messages"][-1].content

        if isinstance(final_response, list):
            final_response = "".join(
                item["text"]
                for item in final_response
                if item.get("type") == "text"
            )

        print('Chef :', final_response)


if __name__ == "__main__":
    main()
