import csv


FILE_NAME = "data.csv"


def read_data():

    try:

        with open(FILE_NAME, "r") as file:

            reader = csv.DictReader(file)

            return list(reader)

    except FileNotFoundError:

        print("data.csv file not found.")
        return []


def show_statistics(data):

    print("\n===== CSV ANALYSIS =====")

    # Record count
    print("Total records:", len(data))

    # Missing values
    missing = 0

    for row in data:

        for value in row.values():

            if value is None or value.strip() == "":
                missing += 1

    print("Missing values:", missing)

    # Duplicate IDs
    ids = set()
    duplicates = set()

    for row in data:

        employee_id = row["id"]

        if employee_id in ids:
            duplicates.add(employee_id)

        ids.add(employee_id)

    print("Duplicate IDs:", duplicates)

    # Salary statistics
    salaries = []

    for row in data:

        try:
            salaries.append(float(row["salary"]))

        except ValueError:
            pass

    if salaries:

        average = sum(salaries) / len(salaries)

        print("Average salary:", average)
        print("Minimum salary:", min(salaries))
        print("Maximum salary:", max(salaries))

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


def main():

    data = read_data()

    if data:
        show_statistics(data)


if __name__ == "__main__":
    main()