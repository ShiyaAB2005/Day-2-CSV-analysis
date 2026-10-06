

employees = []


def add_employee():
    try:
        employee_id = input("Enter employee ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = float(input("Enter salary: "))
        department = input("Enter department: ")

        employee = {
            "id": employee_id,
            "name": name,
            "age": age,
            "salary": salary,
            "department": department
        }

        employees.append(employee)

        print("Employee added successfully.")

    except ValueError:
        print("Please enter valid age and salary.")


def show_employees():
    if not employees:
        print("No employees found.")
        return

    for employee in employees:
        print(employee)


import csv
def read_csv():

    try:
        with open("employees.csv", "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        print("\nTotal records:", len(data))

        # Missing values
        missing = 0

        for row in data:
            for value in row.values():
                if value is None or value.strip() == "":
                    missing += 1

        print("Missing values:", missing)

        # Salary statistics
        salaries = []

        for row in data:
            try:
                salaries.append(float(row["salary"]))
            except ValueError:
                pass

        if salaries:
            print("Average salary:", sum(salaries) / len(salaries))
            print("Minimum salary:", min(salaries))
            print("Maximum salary:", max(salaries))

        # Duplicate IDs
        ids = []
        duplicates = []

        for row in data:
            if row["id"] in ids:
                duplicates.append(row["id"])
            else:
                ids.append(row["id"])

        print("Duplicate IDs:", duplicates)

        # Category-wise statistics
        departments = {}

        for row in data:
            department = row["department"]

            if department not in departments:
                departments[department] = 0

            departments[department] += 1

        print("\nDepartment-wise statistics:")

        for department, count in departments.items():
            print(department, ":", count)

    except FileNotFoundError:
        print("employees.csv file not found.")

def main():

    while True:

        print("\n===== PYTHON EXERCISES =====")
        print("1. Add Employee")
        print("2. Show Employees")
        print("3. Read CSV and Statistics")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            show_employees()

        elif choice == "3":
            read_csv()

        elif choice == "4":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()