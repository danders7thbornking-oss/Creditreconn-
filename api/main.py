from fastapi import FastAPI

app = FastAPI(title="Creditreconn API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
