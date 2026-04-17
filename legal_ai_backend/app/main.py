from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import chat, documents

app = FastAPI(title="Sattam Legal AI Backend")

app.add_middleware(
    CORSMiddleware,
    # FIX: Never use ["*"] in production — lock to your Flutter app origin.
    # For local dev, ["*"] is fine. Change before deployment.
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(documents.router, prefix="/documents", tags=["Documents"])
# FIX: Added prefix so URLs are /chat/ask and /documents/upload
# instead of /ask and /upload (which will conflict if you add more routers)

@app.get("/")
def health_check():
    return {"status": "Sattam Legal AI is running!"}