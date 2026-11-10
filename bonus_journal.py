def make_student(name, score):
    return {"name": name, "score": score}
def add_student(students, name, score):
    student = make_student(name, score)
    students.append(student)
def average_score(students):
    if len(students) == 0:
        return 0
    total = 0
    for s in students:
        total = total + s["score"]
    return total / len(students)
def top_student(students):
    if len(students) == 0:
        return None
    max1=0
    for s in students:
        if s["score"] >max1["score"]:
            max1 = s
    return max1
def print_report(students):
    for s in students:
        print(s["name"] + ": " + str(s["score"]))
    print("Average: " + str(average_score(students)))
    max1 = top_student(students)
    if best is not None:
        print("Top student: " + max1["name"] + " (" + str(max1["score"]) + ")")


students=[]
while True:
    choice = input("Choice: ")
    if choice == "1":
        name = input("Name: ")
        score = int(input("Score: "))
        add_student(students, name, score)
    elif choice == "2":
        print_report(students)
    elif choice == "3":
        break
    else:
        print("Wrong choice")


