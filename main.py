from fastmcp import FastMCP
import random
import json


mcp = FastMCP("Simple Calculator Server")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool
def generate_random_number(
    min_num: int = 0,
    max_num: int = 100
) -> int:
    """Generate a random number."""
    return random.randint(min_num, max_num)


@mcp.resource("info://server")
def server_info() -> str:
    """Get information about the server."""

    info = {
        "name": "Simple Calculator",
        "version": "1.0.0",
        "tools": [
            "add",
            "generate_random_number"
        ],
        "author": "Chitranshu"
    }

    return json.dumps(info, indent=2)


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=8000
    )