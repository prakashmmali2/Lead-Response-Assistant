import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found. Please set it in .env file.")

# Initialize HuggingFace Inference Client
client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=HF_TOKEN
)

SYSTEM_PROMPT = """
You are an AI assistant for a property inspection company.

Strict Rules:
- No emojis.
- No bold formatting.
- No friendly greetings.
- No long explanations.
- Do not list too many possible causes.
- Keep responses under 180 words.
- Use numbered structure exactly as requested.

Structure:
1. Acknowledge issue
2. Likely concern (broad, not specific)
3. 2–4 clarifying questions
4. Safe next steps
5. Suggest inspection if needed
"""


def generate_lead_response(user_input: str) -> str:
    try:
        response = client.chat_completion(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            max_tokens=180,
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating response: {e}"


# ✅ Test Run
if __name__ == "__main__":
    query = "Does the dampness appear only during rainfall or remain afterward?"
    result = generate_lead_response(query)
    print("\nGenerated Response:\n")
    print(result)
