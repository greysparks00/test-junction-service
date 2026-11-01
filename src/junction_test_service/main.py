from fastapi import HTTPException

from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }