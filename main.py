from fastapi import FastAPI

app = FastAPI(
    title = "Sans",
    description = "API description",
    version = "0.1.0",
    docs_url = "/docs",
    redoc_url = "/redoc"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
