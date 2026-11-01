from fastapi import HTTPException

from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    raise HTTPException(status_code=503, detail="Health check failed")