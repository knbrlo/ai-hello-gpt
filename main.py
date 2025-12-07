import sys
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your prompt here\"")
        sys.exit(1)
    
    prompt = sys.argv[1]

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
    
