from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def rootPath():
    return {
        "code": 200,
        "message": "Hello! This is the root route!" 
    }