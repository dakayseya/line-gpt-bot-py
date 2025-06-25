from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
def health_check():
    return PlainTextResponse("LINE GPT Bot is running!")

@app.post("/callback")
async def callback(request: Request):
    body = await request.body()
    print("Received from LINE:", body)
    return PlainTextResponse("OK")
