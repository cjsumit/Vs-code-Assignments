class Student:
    def __init__(self, name, grade):
        # Initialize student with name, grade, and an empty attendance record
        self.name = name
        self.grade = grade
        self.attendance = {}

    def add_attendance(self, date, status):
        #"""Add attendance for a specific date."""
        if status not in ["Present", "Absent"]:
            print("Invalid status. Please enter 'Present' or 'Absent'.")
            return
        self.attendance[date] = status

    def view_attendance(self):
        #"""View all attendance records for the student."""
        if not self.attendance:
            print(f"No attendance recorded for {self.name}.")
        else:
            for date, status in self.attendance.items():
                print(f"{date}: {status}")

    def calculate_attendance_percent(self, total_days):
        if total_days <= 0:
            return 0
        present_days = 0
        for status in self.attendance.values():
            if status == "Present":
                present_days += 1
        attendance_percentage = (present_days / total_days) * 100
        return attendance_percentage



attendance_db = {}  # Dictionary to store Student objects


def add_student(name, grade):
    #"""Add a new student to the system."""
    attendance_db[name] = Student(name, grade)
    print(f"Student {name} added with grade {grade}.")


def update_student(name, grade):
    """Update the grade of an existing student."""
    if name in attendance_db:
        attendance_db[name].grade = grade
        print(f"Student {name} updated with grade {grade}.")
    else:
        print(f"{name} not found.")


def delete_student(name):
    """Delete a student from the system."""
    if name in attendance_db:
        del attendance_db[name]
        print(f"Student {name} removed from the system.")
    else:
        print(f"{name} not found.")


def view_students():
    """View all students and their grades."""
    if attendance_db:
        for name, student in attendance_db.items():
            print(f"{name} - Grade: {student.grade}")
    else:
        print("No students found.")


def search_student(name):
    """Search for a student by name and show their details."""
    if name in attendance_db:
        student = attendance_db[name]
        print(f"Student: {student.name}")
        print(f"Grade: {student.grade}")
        student.view_attendance()
    else:
        print(f"{name} not found.")


def add_attendance(name, date, status):
    """Add attendance record for a student."""
    if name in attendance_db:
        attendance_db[name].add_attendance(date, status)
    else:
        print(f"{name} not found.")


def calculate_attendance_percent(name, total_days):
    """Calculate and display the attendance percentage of a student."""
    if name in attendance_db:
        student = attendance_db[name]
        attendance_percent = student.calculate_attendance_percent(total_days)
        print(f"{name}'s attendance percentage: {attendance_percent:.2f}%")
    else:
        print(f"{name} not found.")


def main():
    """Main menu for the system."""
    while True:
        print("\n--- Students Attendance Management System ---")
        print("1. Add a student")
        print("2. Update a student's grade")
        print("3. Delete a student")
        print("4. View all students")
        print("5. Search for a student")
        print("6. Add attendance for a student")
        print("7. Calculate attendance percentage")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            grade = input("Enter student's grade: ")
            add_student(name, grade)

        elif choice == "2":
            name = input("Enter student's name: ")
            grade = input("Enter new grade: ")
            update_student(name, grade)

        elif choice == "3":
            name = input("Enter student's name: ")
            delete_student(name)

        elif choice == "4":
            view_students()

        elif choice == "5":
            name = input("Enter student's name to search: ")
            search_student(name)

        elif choice == "6":
            name = input("Enter student's name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            status = input("Enter attendance status (Present/Absent): ")
            add_attendance(name, date, status)

        elif choice == "7":
            name = input("Enter student's name: ")
            try:
                total_days = int(input("Enter the total number of school days: "))
                calculate_attendance_percent(name, total_days)
            except ValueError:
                print("Please enter a valid integer for the total days.")

        elif choice == "8":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice! Please select a valid option.")

main()
