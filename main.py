import asyncio, os

from dotenv import load_dotenv  
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools

load_dotenv()

llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command="python",
    args=["C:\\Users\\test\\Documents\\mcp-learning\\servers\\math_server.py"],
)

async def main():
    print("Hello from mcp-learning!")


if __name__ == "__main__":
    asyncio.run(main())
