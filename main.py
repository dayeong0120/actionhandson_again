from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, 00WDSFSFsdfsorld!"}

@app.get("/test")
async def root():
    return "Hello, test page!!"