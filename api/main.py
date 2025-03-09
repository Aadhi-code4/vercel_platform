from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data from data/students.json
data_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "students.json")
with open(data_file_path) as f:
    students = json.load(f)

# Convert students list to a dictionary for faster lookup
students_dict = {student["name"]: student["marks"] for student in students}

@app.get("/api")
def get_marks(name: list[str] = Query([])):  
    marks = [students_dict.get(n, None) for n in name]  # Preserve order
    return {"marks": marks}

@app.get("/")
def read_root():
    return {"message": "Hello, go to /api"}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
