from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transformers import pipeline
from pathlib import Path

app = FastAPI()

# path to the frontend files
frontend_dir = Path(__file__).resolve().parent.parent / "frontend"

# use a small, freely available model, with a fallback if download fails
try:
    generator = pipeline("text-generation", model="distilgpt2")
except Exception:
    def generator(prompt, max_length=400, num_return_sequences=1):
        return [{"generated_text": f"Demo feed for: {prompt}"}]

PROMPT_TEMPLATE = """
You are a fun, smart educator. Give a 5-part microlearning feed on the topic: '{topic}'.

Structure your output as:
1. 💡 Concept: Explain the topic in a simple way
2. 🧠 Analogy: Use a vivid analogy or metaphor
3. ✍️ Quote: A real or generated quote on the topic
4. 🎯 Challenge: A 1-day mini action user can take to apply it
5. 🤖 Fun Fact: Something surprising, meme-worthy, or trivia-like

Keep each section short and easy to read. Use modern, friendly tone.
"""

class Topic(BaseModel):
    topic: str

@app.post("/generate")
async def generate_feed(topic: Topic):
    prompt = PROMPT_TEMPLATE.format(topic=topic.topic)
    result = generator(prompt, max_length=400, num_return_sequences=1)[0]["generated_text"]
    return {"feed": result}

# serve the simple frontend
app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
