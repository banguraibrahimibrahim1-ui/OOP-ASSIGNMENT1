"""
STUDENT RESULTS MANAGEMENT SYSTEM
PROG211 - Object-Oriented Programming (OOP1)

A console-based application for registering students, recording marks,
calculating totals and averages, assigning grades, and displaying reports.
"""

class Student:
    student_count = 0

    def __init__(self, student_id, name):
        self.student_id = student_id.strip().upper()
        self.name = name.strip()
        self.results = {}
        Student.student_count += 1

    def add_result(self, subject, mark):
        subject = subject.strip().title()
        if not subject:
            raise ValueError("Subject name cannot be empty.")
        if not isinstance(mark, (int, float)) or isinstance(mark, bool):
            raise ValueError("Mark must be a number.")
        if not 0 <= mark <= 100:
            raise ValueError("Mark must be between 0 and 100.")
        self.results[subject] = float(mark)

    def calculate_total(self):
        return sum(self.results.values())

    def calculate_average(self):
        if not self.results:
            return 0.0
        return self.calculate_total() / len(self.results)

    def get_grade(self):
        average = self.calculate_average()
        if average >= 80:
            return "A"
        if average >= 70:
            return "B"
        if average >= 60:
            return "C"
        if average >= 50:
            return "D"
        return "F"

    def display_result(self):
        print("\n" + "=" * 48)
        print("             STUDENT RESULT REPORT")
        print("=" * 48)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        if not self.results:
            print("No subject results have been recorded.")
        else:
            print("-" * 48)
            print(f"{'Subject':<25}{'Mark':>10}")
            print("-" * 48)
            for subject, mark in self.results.items():
                print(f"{subject:<25}{mark:>10.2f}")
            print("-" * 48)
            print(f"{'Total':<25}{self.calculate_total():>10.2f}")
            print(f"{'Average':<25}{self.calculate_average():>10.2f}")
            print(f"{'Grade':<25}{self.get_grade():>10}")
        print("=" * 48)


class ResultsManagementSystem:
    def __init__(self, school_name="Student Results Management System"):
        self.school_name = school_name
        self.students = {}  # Student ID is the key; Student object is the value.

    @classmethod
    def system_description(cls):
        return (
            f"{cls.__name__}: a console application for managing "
            "student academic results."
        )

    def register_student(self, student_id, name):
        student_id = student_id.strip().upper()
        name = name.strip()
        if not student_id:
            raise ValueError("Student ID cannot be empty.")
        if not name:
            raise ValueError("Student name cannot be empty.")
        if student_id in self.students:
            raise ValueError("A student with this ID already exists.")
        self.students[student_id] = Student(student_id, name)
        print(f"Student {name} registered successfully.")

    def record_result(self, student_id, subject, mark):
        student_id = student_id.strip().upper()
        if student_id not in self.students:
            raise ValueError("Student ID was not found.")
        self.students[student_id].add_result(subject, mark)
        print("Result recorded successfully.")

    def view_student_result(self, student_id):
        student_id = student_id.strip().upper()
        if student_id not in self.students:
            raise ValueError("Student ID was not found.")
        self.students[student_id].display_result()

    def display_all_students(self):
        if not self.students:
            print("\nNo students have been registered.")
            return
        print("\n" + "=" * 68)
        print(f"{self.school_name.upper():^68}")
        print("=" * 68)
        print(f"{'Student ID':<15}{'Student Name':<25}{'Average':>12}{'Grade':>10}")
        print("-" * 68)
        for student in self.students.values():
            if student.results:
                average = student.calculate_average()
                grade = student.get_grade()
                print(f"{student.student_id:<15}{student.name:<25}{average:>12.2f}{grade:>10}")
            else:
                print(f"{student.student_id:<15}{student.name:<25}{'N/A':>12}{'N/A':>10}")
        print("=" * 68)

    def calculate_class_average(self):
        marks = [
            mark
            for student in self.students.values()
            for mark in student.results.values()
        ]
        return sum(marks) / len(marks) if marks else 0.0

    def load_sample_data(self):
        sample_students = [
            ("ST001", "John Kamara", {"Mathematics": 80, "English": 75, "Computer Studies": 85}),
            ("ST002", "Mary Sesay", {"Mathematics": 65, "English": 70, "Computer Studies": 60}),
            ("ST003", "Ibrahim Koroma", {"Mathematics": 45, "English": 50, "Computer Studies": 40}),
        ]
        for student_id, name, results in sample_students:
            self.register_student(student_id, name)
            for subject, mark in results.items():
                self.record_result(student_id, subject, mark)


def get_mark_from_user():
    try:
        return float(input("Enter mark (0-100): ").strip())
    except ValueError:
        raise ValueError("Please enter a valid number.")


def main():
    system = ResultsManagementSystem()
    print("=" * 58)
    print("          STUDENT RESULTS MANAGEMENT SYSTEM")
    print("=" * 58)
    print(ResultsManagementSystem.system_description())

    while True:
        print("\nMAIN MENU")
        print("1. Register student")
        print("2. Record student result")
        print("3. View one student's result")
        print("4. Display all students")
        print("5. Calculate overall class average")
        print("6. Load sample data")
        print("7. Exit")
        choice = input("Choose an option (1-7): ").strip()

        try:
            if choice == "1":
                system.register_student(
                    input("Enter student ID: "),
                    input("Enter student name: ")
                )
            elif choice == "2":
                student_id = input("Enter student ID: ")
                subject = input("Enter subject name: ")
                mark = get_mark_from_user()
                system.record_result(student_id, subject, mark)
            elif choice == "3":
                system.view_student_result(input("Enter student ID: "))
            elif choice == "4":
                system.display_all_students()
            elif choice == "5":
                print(f"Overall class average: {system.calculate_class_average():.2f}%")
            elif choice == "6":
                system.load_sample_data()
                print("Sample data loaded successfully.")
            elif choice == "7":
                print("Thank you for using the Student Results Management System.")
                break
            else:
                print("Invalid option. Please choose a number from 1 to 7.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
