students = [
    {'name': 'Tina', 'hometown': 'Portland', 'favorite_food': 'puppy chow'},
    {'name': 'Klaus', 'hometown': 'Frankfurt', 'favorite_food': 'pizza'},
    {'name': 'Julia', 'hometown': 'Houston', 'favorite_food': 'shrimp'}
]


def list_names(students):
    position = 1
    for first_name in students:
        print(str(position), first_name['name'])
        position += 1

def get_new_student():
    new_student = {'name': input("Enter student name: "), 'hometown': input("Enter student hometown: "),
                   'favorite_food': input("Enter student favorite food: ")}
    return new_student

while True:
    action = input("Enter an action (add, view, quit): ")

    if action == "add":
        new_student = get_new_student()
        students.append(new_student)

    elif action == "view":
        list_names(students)
        index = int(input(f"Enter the student index to view. Select from 1-{len(students)} ")) - 1
        selection_index = index + 1
        student = students[index]
        print(f"Student {selection_index} is {student['name']}")
        choice = input("What would you like to know? (hometown or favorite food): ")
        if choice.lower() == 'hometown':
            print(f"{student['name']} is from {student[choice]}")
        elif choice.lower() == 'favorite food':
            print(f"{student['name']}'s favorite food is {student[choice]}")

    elif action == "quit":
        print('Goodbye!')
        break

    else:
        print("Invalid action. Try again.")


