from fastmcp import FastMCP

mcp = FastMCP("test")

@mcp.tool
def test() -> str:
    """Test tool"""
    return "works"

app = mcp.get_app()
