from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS to allow GET requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data from data/students.json
data_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'students.json')
with open(data_file_path) as f:
    students = json.load(f)

@app.get("/api")
def get_marks(names: list[str] = Query(None)):
    marks = [student['marks'] for student in students if student['name'] in names]
    return {"marks": marks}

# Example root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
