import uuid
class CRUD:

    def __init__(self):
        self._storage = {}

    def create(self, key, obj):
        if key in self._storage:
            print("Record already exists!")
        else:
            self._storage[key] = obj
            print("Record created successfully!")

    def read(self, key):
        return self._storage.get(key)

    def update(self, key, **kwargs):
        obj = self._storage.get(key)
        if not obj:
            print("Record not found!")
            return

        for attr, value in kwargs.items():
            if hasattr(obj, attr):
                setattr(obj, attr, value)

        print("Record updated successfully!")

    def delete(self, key):
        if key in self._storage:
            del self._storage[key]
            print("Record deleted successfully!")
        else:
            print("Record not found!")

    def display_all(self):
        if not self._storage:
            print("No records found.")
            return

        for obj in self._storage.values():
            print(obj)
            print("-------------------")

class Subject(CRUD):

    class SubjectData:
        def __init__(self, name):
            self.id = str(uuid.uuid4())
            self.name = name

        def __str__(self):
            return f"Subject ID: {self.id} | Name: {self.name}"

    def add_subject(self, name):
        subject = self.SubjectData(name)
        self.create(subject.id, subject)
        print("Generated Subject ID:", subject.id)

class Student(CRUD):

    class StudentData:
        def __init__(self, name, usn):
            self.name = name
            self.usn = usn
            self.subject_ids = []

    def add_student(self, name, usn):
        student = self.StudentData(name, usn)
        self.create(usn, student)

    def assignSubstoStudent(self, subject_manager):

        usn = input("Enter USN of student: ")
        student = self.read(usn)

        if not student:
            print("Student not found!")
            return

        choice = input("Do you want to assign subjects? (yes/no): ").lower()

        if choice != "yes":
            return

        if not subject_manager._storage:
            print("No subjects available. Add subjects first.")
            return

        print("\nAvailable Subjects:")
        for sid, sub in subject_manager._storage.items():
            print(f"{sid} | {sub.name}")

        try:
            total_sub = int(input("Enter number of subjects to assign: "))
        except ValueError:
            print("Invalid number!")
            return

        for _ in range(total_sub):
            sub_id = input("Enter Subject UUID: ")

            if sub_id in subject_manager._storage:
                if sub_id not in student.subject_ids:
                    student.subject_ids.append(sub_id)
                    print("Subject assigned successfully!")
                else:
                    print("Subject already assigned.")
            else:
                print("Invalid Subject UUID!")

    # Display single student with subject names
    def display_student(self, usn, subject_manager):
        student = self.read(usn)

        if not student:
            print("Student not found!")
            return

        print(f"\nName: {student.name}")
        print(f"USN: {student.usn}")

        if not student.subject_ids:
            print("Subjects: None")
        else:
            print("Subjects:")
            for sid in student.subject_ids:
                subject = subject_manager._storage.get(sid)
                if subject:
                    print(f"- {subject.name}")

student_manager = Student()
subject_manager = Subject()

while True:
    print("\n=========== MENU ===========")
    print("1. Manage Student")
    print("2. Manage Subject")
    print("3. Exit")

    main_choice = int(input("Enter choice: "))

    match main_choice:

        case 1:
            print("\n1. Add Student")
            print("2. View Student")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. View All Students")
            print("6. Assign subjects to student")
            print("------------------------")

            ch = int(input("Enter choice: "))

            if ch == 1:
                name = input("Enter name: ")
                usn = input("Enter USN: ")
                student_manager.add_student(name, usn)

            elif ch == 2:
                usn = input("Enter USN: ")
                student_manager.display_student(usn, subject_manager)

            elif ch == 3:
                usn = input("Enter USN: ")
                new_name = input("Enter new name: ")
                student_manager.update(usn, name=new_name)

            elif ch == 4:
                usn = input("Enter USN: ")
                student_manager.delete(usn)

            elif ch == 5:
                if not student_manager._storage:
                    print("No students found.")
                else:
                    for usn in student_manager._storage:
                        student_manager.display_student(usn, subject_manager)
                        print("----------------------")

            elif ch == 6:
                student_manager.assignSubstoStudent(subject_manager)

        #  SUBJECT MENU 
        case 2:
            print("\n1. Add Subject")
            print("2. View All Subjects")
            print("3. Delete Subject")

            ch = int(input("Enter choice: "))

            if ch == 1:
                try:
                    total = int(input("How many subjects do you want to add? "))
                except ValueError:
                    print("Invalid number!")
                    continue

                for i in range(total):
                    print(f"\nAdding Subject {i+1}")
                    name = input("Enter subject name: ")
                    subject_manager.add_subject(name)

            elif ch == 2:
                subject_manager.display_all()

            elif ch == 3:
                sid = input("Enter Subject ID: ")
                subject_manager.delete(sid)

        #  EXIT condition
        case 3:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice!")
