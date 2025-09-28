# Claire MCP Server

FastMCP server template with all patterns in one clean example.

## Setup

### 1. Get GitHub Token
- Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
- Generate new token with `repo` scope
- Copy the `ghp_xxxx...` token

### 2. Set Environment Variables
```bash
export GITHUB_TOKEN="ghp_yourtoken"
export GITHUB_REPO="yourusername/your-repo"
```

### 3. Configure Claude Desktop

Add to Claude Desktop config:

```json
{
  "mcpServers": {
    "claire-tools": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://${GITHUB_TOKEN}@github.com/${GITHUB_REPO}.git",
        "claire-mcp"
      ]
    }
  }
}
```

### 4. Restart Claude Desktop

## Development

The `process_file` example shows all FastMCP patterns:
- Required params (`path`)
- Optional with defaults (`output_format`, `max_lines`)
- Optional that can be None (`skip_patterns`)
- Boolean flags (`include_metadata`)
- Field descriptions for strict formats (`url`)
- Dict return type for structured data

Just replace with your own tools following the same patterns!
