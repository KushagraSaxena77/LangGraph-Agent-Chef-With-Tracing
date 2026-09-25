# LangGraph Chef Agent

An AI powered personal chef agent built with LangGraph, LangChain, Google Gemini, and Tavily.

The project demonstrates how to build a tool using AI agent that can understand natural language requests, search the web when required, maintain conversational context, and generate concise and practical cooking guidance.

---

## Overview

LangGraph Chef Agent is a conversational AI chef designed to help users with cooking and recipe related tasks.

Instead of simply generating a response from a language model, the agent can decide when external information is required and use a web search tool to retrieve relevant information before generating its final response.

The project uses LangGraph for agent orchestration and state management, LangChain for the agent framework and tool integration, Google Gemini as the language model, and Tavily for web search.

### Example

A user can ask:

> Give me a recipe for Aloo Paratha.

The agent can determine whether additional information is required, perform a web search using Tavily, and then generate a concise recipe with ingredients and instructions.

---

## Features

### AI Chef Agent

Interact with the system using natural language and ask questions related to cooking, recipes, ingredients, and meal preparation.

### Web Search

The agent can use Tavily to search the web when external information is required.

### Conversational Context

The application is designed around LangGraph's state and persistence capabilities, allowing conversations to maintain context across interactions when using the LangGraph runtime.

### Tool Calling

The agent can decide when to call external tools instead of relying entirely on the language model.

### Google Gemini

Google Gemini is used as the underlying language model for understanding requests and generating responses.

### LangGraph Orchestration

LangGraph manages the agent workflow and provides the foundation for stateful agent execution.

### LangGraph Studio

The project can be run using the LangGraph development server and inspected through LangGraph Studio.

### Concise Responses

The chef agent is instructed to provide simple, practical, and easy to follow cooking instructions.

---

## Architecture

<img width="425" height="360" alt="image" src="https://github.com/user-attachments/assets/bc2b7f9f-d5ea-4dec-a1c9-d9575f40256d" />
<img width="423" height="263" alt="image" src="https://github.com/user-attachments/assets/a3adc003-2096-4923-8cec-444356ea1bf2" />

---

The high level execution flow is:
```

User Request
     |
     v
LangGraph Agent
     |
     v
Gemini decides what to do
     |
     +------ No external information required
     |                  |
     |                  v
     |             Generate Response
     |
     +------ Web information required
                        |
                        v
                  Tavily Search
                        |
                        v
                  Gemini processes
                        |
                        v
                  Final Response
```

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| LangGraph | Agent orchestration and state management |
| LangChain | Agent framework and tool integration |
| Google Gemini | Large language model |
| Tavily | Web search |
| LangGraph Studio | Agent development and debugging |
| UV | Python environment and dependency management |
| Git | Version control |
| GitHub | Source code hosting |

---

## Project Structure

```
langgraph-chef-agent/
│
├── main.py
├── langgraph.json
├── .env
├── .gitignore
├── README.md
│
└── .venv/
```

### `main.py`

Contains the main agent implementation, Gemini configuration, system prompt, and Tavily web search tool.

### `langgraph.json`

Defines the LangGraph application and tells the LangGraph runtime where the agent is located.

### `.env`

Stores API credentials and environment variables.

This file must never be committed to GitHub.

### `.gitignore`

Prevents sensitive files and local development files from being uploaded to the repository.

---

# Getting Started

## Prerequisites

Before running the project, make sure you have:

* Python 3.10 or newer
* Git
* UV
* A Google Gemini API key
* A Tavily API key

---

# 1. Clone the Repository

Clone the repository to your local machine.

```bash
git clone https://github.com/YOUR_USERNAME/langgraph-chef-agent.git
```

Move into the project directory:

```bash
cd langgraph-chef-agent
```

---

# 2. Install UV

UV is used for Python environment and dependency management.

If UV is not already installed, install it using:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your terminal after installation if required.

Verify the installation:

```bash
uv --version
```

---

# 3. Create a Virtual Environment

Create a virtual environment:

```bash
uv venv
```

Activate it.

### macOS and Linux

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

---

# 4. Install Dependencies

Install the required packages:

```bash
uv pip install langchain langgraph langchain-google-genai tavily-python python-dotenv
```

If you are using a `pyproject.toml`, dependencies can instead be installed with:

```bash
uv sync
```

---

# 5. Configure API Keys

Create a `.env` file in the root directory:

```text
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
LANGSMITH_TRACING=false
```

Replace the placeholder values with your actual API keys.

Do not commit the `.env` file to GitHub.

---


# 7. Configure LangGraph

Create `langgraph.json` in the project root:

```json
{
  "dependencies": ["."],
  "graphs": {
    "chef": "./main.py:agent"
  },
  "env": ".env"
}
```

The important part is:

```json
"graphs": {
  "chef": "./main.py:agent"
}
```

This tells LangGraph that the graph named `chef` is available through the `agent` object inside `main.py`.


---

# 11. Run the Agent with LangGraph

Start the LangGraph development server:

```bash
uv run langgraph dev
```

You should see output similar to:

```text
API: http://127.0.0.1:2024
Studio UI: https://smith.langchain.com/studio/
```

The API will be available locally through:

```text
http://127.0.0.1:2024
```

---

# 12. Open LangGraph Studio

Open the Studio URL provided by the terminal.

LangGraph Studio allows you to interact with the agent and inspect its execution.

You can observe:

```text
User Input
    |
    v
Agent
    |
    +---- Gemini
    |
    +---- Tavily
    |
    v
Final Response
```

This is particularly useful for debugging agent workflows and understanding tool calls.



---

# How the Agent Works

The agent follows a tool using workflow.

### Step 1: User Input

The user sends a natural language request.

```text
Give me a recipe for Aloo Paratha.
```

### Step 2: Agent Reasoning

Gemini analyses the request and determines how to respond.

### Step 3: Tool Selection

If external information is required, the agent calls:

```text
web_search()
```

### Step 4: Web Search

Tavily searches the web and returns relevant information.

### Step 5: Response Generation

Gemini processes the available information and generates the final response.

### Step 6: User Response

The final recipe is returned to the user.

---


# Environment Variables

The application uses the following environment variables:

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | Google Gemini API authentication |
| `TAVILY_API_KEY` | Tavily web search authentication |
| `LANGSMITH_TRACING` | Enables or disables LangSmith tracing |

Example:

```env
GOOGLE_API_KEY=your_key
TAVILY_API_KEY=your_key
LANGSMITH_TRACING=false
```

---

# LangGraph Persistence

One important aspect of this project is conversational state.

When the application is run through the LangGraph runtime, persistence is managed by the runtime rather than manually creating an `InMemorySaver`.

For local experimentation outside the LangGraph runtime, an in memory checkpointer can be useful.

However, for the LangGraph application defined in `langgraph.json`, the runtime manages the persistence layer.

This allows the application to work with conversation threads without implementing the persistence mechanism manually.

---





# Troubleshooting

## Google API Key Not Found

Check that `.env` exists in the project root:

```text
langgraph-chef-agent/
├── .env
├── main.py
└── langgraph.json
```

Check that the variable is named:

```env
GOOGLE_API_KEY=your_key
```

---

## Tavily API Key Not Found

Check:

```env
TAVILY_API_KEY=your_key
```

and ensure it is loaded before creating the Tavily client.

---

## LangGraph Cannot Load the Graph

Check `langgraph.json`:

```json
{
  "dependencies": ["."],
  "graphs": {
    "chef": "./main.py:agent"
  },
  "env": ".env"
}
```

Also make sure `main.py` contains:

```python
agent = create_agent(...)
```


---

# Contributing

Contributions are welcome.


---

# Author

**Kushagra Saxena**

---

> **`LangGraph Chef Agent`**
