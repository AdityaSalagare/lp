# SnipFeedAI

SnipFeedAI is a lightweight demo that generates bite-sized, AI-powered knowledge feeds. A user enters a topic, and the backend uses a free, open-source text generation model to build a five item feed:

1. 💡 Concept
2. 🧠 Analogy
3. ✍️ Quote
4. 🎯 Challenge
5. 🤖 Fun Fact

The frontend is a minimalist Tailwind page, and the backend is a small FastAPI service.

## Structure
- `backend/app.py` – FastAPI server exposing a `/generate` endpoint
- `backend/requirements.txt` – Python dependencies
- `frontend/index.html` – simple UI that calls the backend

## Run locally
```bash
pip install -r SnipFeedAI/backend/requirements.txt
uvicorn SnipFeedAI.backend.app:app --reload
# open frontend/index.html in a browser
```
