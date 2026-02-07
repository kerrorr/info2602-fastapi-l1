from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
def hello_world():
    return 'Hello, World!'

from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
async def hello_world():
    return 'Hello, World!'

### New Function
@app.get('/students')
async def get_students():
    return data
### End of new function

@app.get('/students/{id}')
async def get_student(id):
  for student in data: 
    if student['id'] == id: 
      return student
    
@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref: 
              filtered_students.append(student) 
        return filtered_students
    return data

@app.get("/stats")
async def get_stats():
    valid_meals = ["Chicken", "Fish", "Vegetable"]
    valid_programmes = [
        "Computer Science (Major)",
        "Computer Science (Special)",
        "Information Technology (Major)",
        "Information Technology (Special)"
    ]

    stats = {}


    for meal in valid_meals:
        stats[meal] = 0
    for prog in valid_programmes:
        stats[prog] = 0

    
    for student in data:
        meal = student.get("pref")
        prog = student.get("programme")

        if meal in stats:
            stats[meal] += 1
        if prog in stats:
            stats[prog] += 1

    return stats

#Exercise 2

@app.get("/add/{a}/{b}")
async def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract/{a}/{b}")
async def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply/{a}/{b}")
async def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide/{a}/{b}")
async def divide(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": a / b}