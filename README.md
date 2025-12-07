# ai-hello-gpt

A simple command-line interface that calls the GPT-4 API. This project demonstrates the basics of working with OpenAI's API in Python.

## Features

- Send prompts to GPT-4 from the command line
- Simple and lightweight implementation
- Easy to understand and extend

## Prerequisites

- Python 3.8 or higher (or Docker)
- An OpenAI API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/knbrlo/ai-hello-gpt.git
cd ai-hello-gpt
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:

Copy the example environment file and add your API key:

```bash
cp .env.example .env
```

Then edit `.env` and replace the placeholder with your actual API key:

```
OPENAI_API_KEY=your-api-key-here
```

Alternatively, you can export the key directly in your terminal session:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Note: Never commit your `.env` file to version control. The `.gitignore` file is configured to exclude it.

## Usage

Run the CLI with a prompt:

```bash
python main.py "Hello, GPT!"
```

Example output:

```
Hello! How can I assist you today?
```

## Usage with Docker

If you prefer not to install Python locally, you can use Docker instead.

1. Build the Docker image:

```bash
docker build -t ai-hello-gpt .
```

2. Run with your API key:

```bash
# Option 1: Pass the key directly
docker run --rm -e OPENAI_API_KEY="your-api-key-here" ai-hello-gpt "Hello, GPT!"

# Option 2: Use your .env file
docker run --rm --env-file .env ai-hello-gpt "Hello, GPT!"
```

Alternatively, use docker-compose:

```bash
docker compose run --rm gpt-cli "Hello, GPT!"
```

## Project Structure

```
ai-hello-gpt/
├── main.py              # Entry point and CLI logic
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment file
├── Dockerfile           # Docker image configuration
├── docker-compose.yml   # Docker Compose configuration
└── README.md            # This file
```

## Dependencies

- `openai` - Official OpenAI Python client
- `python-dotenv` - Environment variable management

## Configuration

| Environment Variable | Description | Required |
|---------------------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

## Learning Objectives

This project covers:

- Making API calls to OpenAI's GPT-4
- Handling API responses in Python
- Building a simple CLI application
- Managing environment variables and API keys securely

## License

MIT
