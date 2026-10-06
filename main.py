import json


FILE_NAME = "employees.json"




def load_data():

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Invalid JSON file.")
        return []


def save_data(employees):

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(employees, file, indent=4)

    except OSError as error:
        print("Error saving data:", error)

def add_employee(employees):

    try:

        employee_id = input("Enter ID: ")

        for employee in employees:
            if employee["id"] == employee_id:
                print("Employee ID already exists.")
                return

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
        save_data(employees)

        print("Employee added successfully.")

    except ValueError:
        print("Please enter valid age and salary")

def update_employee(employees):

    employee_id = input("Enter ID to update: ")

    for employee in employees:

        if employee["id"] == employee_id:

            try:
                employee["name"] = input("Enter new name: ")
                employee["age"] = int(input("Enter new age: "))
                employee["salary"] = float(input("Enter new salary: "))
                employee["department"] = input("Enter new department: ")

                save_data(employees)

                print("Employee updated successfully.")
                return

            except ValueError:
                print("Invalid age or salary.")
                return

    print("Employee not found.")


def delete_employee(employees):

    employee_id = input("Enter ID to delete: ")

    for employee in employees:

        if employee["id"] == employee_id:

            employees.remove(employee)
            save_data(employees)

            print("Employee deleted successfully.")
            return

    print("Employee not found.")

def search_employee(employees):

    keyword = input("Enter ID or name: ").lower()

    found = False

    for employee in employees:

        if (
            keyword in employee["id"].lower()
            or keyword in employee["name"].lower()
        ):
            print(employee)
            found = True

    if not found:
        print("Employee not found.")

def list_employees(employees):

    if not employees:
        print("No employees found.")
        return

    for employee in employees:
        print(employee)

def filter_employees(employees):

    department = input("Enter department: ").lower()

    found = False

    for employee in employees:

        if employee["department"].lower() == department:
            print(employee)
            found = True

    if not found:
        print("No employees found.")

def sort_employees(employees):

    print("\n1. Sort by Name")
    print("2. Sort by Salary")

    choice = input("Enter choice: ")

    if choice == "1":

        result = sorted(
            employees,
            key=lambda employee: employee["name"].lower()
        )

    elif choice == "2":

        result = sorted(
            employees,
            key=lambda employee: employee["salary"],
            reverse=True
        )

    else:
        print("Invalid choice.")
        return

    for employee in result:
        print(employee)
def statistics(employees):

    if not employees:
        print("No employee data.")
        return

    salaries = [
        employee["salary"]
        for employee in employees
    ]

    print("\nTotal Employees:", len(employees))
    print("Average Salary:", sum(salaries) / len(salaries))
    print("Highest Salary:", max(salaries))
    print("Lowest Salary:", min(salaries))

def main():

    employees = load_data()

    while True:

        print("\n================================")
        print("     EMPLOYEE MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. List Employees")
        print("6. Filter Employees")
        print("7. Sort Employees")
        print("8. Statistics")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_employee(employees)

        elif choice == "2":
            update_employee(employees)

        elif choice == "3":
            delete_employee(employees)

        elif choice == "4":
            search_employee(employees)

        elif choice == "5":
            list_employees(employees)

        elif choice == "6":
            filter_employees(employees)

        elif choice == "7":
            sort_employees(employees)

        elif choice == "8":
            statistics(employees)

        elif choice == "9":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()