employees = {}


def menu():
    print("\n--- EMPLOYEE MANAGER ---")
    print("1. Add employee")
    print("2. View employees")
    print("3. Search employee")
    print("4. Exit")


def add_employee():
    name = input("Enter employee name: ")

    try:
        age = int(input("Enter employee age: "))

        if age < 18:
            print("Employee must be at least 18 years old")
            return

        employees[name] = age
        print("Employee added successfully")

    except ValueError:
        print("Invalid age")


def view_employees():
    if not employees:
        print("No employees found")
        return

    for name, age in employees.items():
        print(f"Name: {name} | Age: {age}")


def search_employee():
    name = input("Enter employee name: ")

    if name in employees:
        print(f"Age: {employees[name]}")
    else:
        print("Employee not found")


while True:
    menu()
    option = input("Choose an option: ")

    if option == "1":
        add_employee()

    elif option == "2":
        view_employees()

    elif option == "3":
        search_employee()

    elif option == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
