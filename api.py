from fastapi import FastAPI
app = FastAPI() #api
@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}