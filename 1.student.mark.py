# Student Mark Management System (No OOP)

students = []    # store student info: [{id, name, DoB}]
courses = []     # store course info: [{id, name}]
marks = {}       # store marks: {course_id: {student_id: mark}}

def input_students():
    n = int(input("Enter number of students: "))
    for _ in range(n):
        sid = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Date of birth: ")
        students.append({"id": sid, "name": name, "DoB": dob})
    print("Students added successfully!\n")

def input_courses():
    n = int(input("Enter number of courses: "))
    for _ in range(n):
        cid = input("Course ID: ")
        cname = input("Course name: ")
        courses.append({"id": cid, "name": cname})
    print("Courses added successfully!\n")

def input_marks():
    if not courses or not students:
        print("Please input students and courses first!\n")
        return

    print("\nAvailable courses:")
    for c in courses:
        print(f"- {c['id']} | {c['name']}")

    cid = input("Enter course ID to input marks: ")

    # check if course ID exists
    course_exists = any(c["id"] == cid for c in courses)
    if not course_exists:
        print("Course not found!\n")
        return

    if cid not in marks:
        marks[cid] = {}

    print("\nEnter marks for students:")
    for s in students:
        mark = float(input(f"Mark for {s['name']} (ID: {s['id']}): "))
        marks[cid][s["id"]] = mark

    print("Marks added successfully!\n")

def list_students():
    print("\n----- Student List -----")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['DoB']}")
    print()

def list_courses():
    print("\n----- Course List -----")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")
    print()

def show_marks():
    if not marks:
        print("No marks available yet!\n")
        return

    cid = input("Enter course ID to view marks: ")

    if cid not in marks:
        print("No marks for this course!\n")
        return

    print(f"\n----- Marks for course {cid} -----")
    for s in students:
        sid = s["id"]
        if sid in marks[cid]:
            print(f"{s['name']} ({sid}): {marks[cid][sid]}")
    print()

def main():
    while True:
        print("\n===== Student Mark Management =====")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a course")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_marks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again!")

main()
`
