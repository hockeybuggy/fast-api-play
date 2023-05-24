from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse("/ping")


def get_current_timestamp() -> int:
    return int(datetime.now().timestamp())


@app.get("/ping")
async def ping():
    current_timestamp = get_current_timestamp()
    return {"pong": current_timestamp}
