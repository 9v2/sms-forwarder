from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import List, Dict

app = FastAPI()

# In-memory storage, you can use any desired storage.
messages: List[Dict] = []

@app.get("/forward")
async def forward_sms(
    msg: str = Query(..., description="The SMS message content"),
    time: str = Query(..., description="Time when the message was received"),
    in_number: str = Query(..., alias="in-number", description="Sender's phone number"),
    filter_name: str = Query(..., alias="filter-name", description="Name/identifier of the phone")
):
    message = {
        "message": msg,
        "time": time,
        "from": in_number,
        "device": filter_name
    }
    messages.append(message)
    return {"status": "saved", "count": len(messages)}

@app.get("/messages")
async def get_all_messages():
    return {"messages": messages} # it will return all received sms message, it should be private!
