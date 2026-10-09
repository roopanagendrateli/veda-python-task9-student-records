def display_students(names, marks):
    print("\n--- Student Records ---")
    for i in range(len(names)):
        print(f"{names[i]}: {marks[i]} marks")


def search_student(names, marks):
    name = input("Enter the student name to search: ").strip()

    for i in range(len(names)):
        if names[i].lower() == name.lower():
            print(f"{names[i]} scored {marks[i]} marks.")
            return

    print("Student not found.")


def sort_students(names, marks):
    students = sorted(zip(names, marks), key=lambda student: student[1])

    print("\n--- Students Sorted by Marks (Lowest to Highest) ---")
    for name, mark in students:
        print(f"{name}: {mark} marks")


def show_highest_lowest(names, marks):
    highest_index = marks.index(max(marks))
    lowest_index = marks.index(min(marks))

    print(
        f"\nHighest score: {names[highest_index]} "
        f"with {marks[highest_index]} marks"
    )
    print(
        f"Lowest score: {names[lowest_index]} "
        f"with {marks[lowest_index]} marks"
    )


def main():
    names = []
    marks = []

    print("=" * 40)
    print("       STUDENT RECORDS SYSTEM")
    print("=" * 40)

    try:
        count = int(input("How many students do you want to enter? "))

        if count <= 0:
            print("Please enter a number greater than zero.")
            return

        for i in range(count):
            print(f"\nStudent {i + 1}")
            name = input("Enter student name: ").strip()

            if not name:
                print("Name cannot be empty. Please try again.")
                return

            score = float(input("Enter marks (0-100): "))

            if score < 0 or score > 100:
                print("Marks must be between 0 and 100.")
                return

            names.append(name)
            marks.append(score)

        while True:
            print("\n--- MENU ---")
            print("1. Display all students")
            print("2. Search for a student")
            print("3. Sort students by marks")
            print("4. Show highest and lowest scores")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                display_students(names, marks)
            elif choice == "2":
                search_student(names, marks)
            elif choice == "3":
                sort_students(names, marks)
            elif choice == "4":
                show_highest_lowest(names, marks)
            elif choice == "5":
                print("Thank you for using Student Records System!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

    except ValueError:
        print("Invalid input. Please enter numbers correctly.")


if __name__ == "__main__":
    main()