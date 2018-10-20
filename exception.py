all_student = [
    {"name": "Vignesh", "id": 100, "dept": "IT"},
    {"name": "Bala", "id": 200, "dept": "CSE"},
    {"name": "Rachel", "id": 300, "dept": "IT"},
    {"name": "Madhu", "id": 400, "dept": "ECE"}
]

database = {
    "student": all_student
}

try:
    print(all_student[1]["last_name"])
except KeyError:
    print("Error getting Last Name")
