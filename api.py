from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from core import generate_password

app = FastAPI(
    title="Password Generato",
    description="A simple API to generate secure passwords",
    version="1.0.0"
)

class PasswordResponse(BaseModel):
    password: str
    length: int
    numbers: bool
    special_characters: bool

@app.get("/generate", response_model=PasswordResponse, summary="Generate password")
def generate(
    min_length: int = Query(12, ge=6, le=128, description="Minimum length of the password 6-128"),
    numbers: bool = Query(True, description="Include numbers in the password"),
    special_characters: bool = Query(True, description="Include special characters in the password")
):
    try:
        pwd = generate_password(min_length, numbers, special_characters)
        return PasswordResponse(
            password=pwd,
            length=len(pwd),
            numbers=numbers,
            special_characters=special_characters
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))