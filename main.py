from fastapi import FastAPI

app = FastAPI()

@app.post("/hello")
def hello_world(text: str):
    return {"message": "Hello Universe!"}

# To run fast api command: uvicorn fast_api_app:app --reload
