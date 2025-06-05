import os
from groq import Groq
from dotenv import load_dotenv
from models import StoryRequest

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)

def generate_prompt(data: StoryRequest) -> str:
    prompt = f"You are a creative AI that writes {data.type}s.\n"
    prompt += f"Tone: {data.tone}\nGenre: {data.genre}\nLength: {data.length} words\n"
    if data.title:
        prompt += f"Title: {data.title}\n"
    if data.characters:
        prompt += f"Characters: {', '.join(data.characters)}\n"
    prompt += "Start your text now:"
    return prompt

def get_generated_text(data: StoryRequest) -> str:
    prompt = generate_prompt(data)
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content
