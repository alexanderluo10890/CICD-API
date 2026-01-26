from fastapi import FastAPI

app = FastAPI(title="CI/CD Mini API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/echo/{msg}")
def echo(msg: str):
    return {"echo": msg}
