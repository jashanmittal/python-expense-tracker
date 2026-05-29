import json
import time

expenses = []

running = True

def save():
    with open("expense.json", "w") as file:
        json.dump(expenses, file)
        print("Saved Successfully")


def load():
    global expenses
    try:
        with open("expense.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []


def menu():
    print("Which feature would you like to use?\n")
    print("1. Add expense\n2. View expense\n3. Total Expenses\n4. Exit")
    choice = input()

    if choice == "4":
        save()
        exit()

    elif choice == "3":
        total = sum(expense["Amount"] for expense in expenses)
        print(f"Total expenses are {total}")
        return

    elif choice == "1":
        amount = input("Enter the amount: \n")
        try:
            amount = float(amount)
        except ValueError:
            print("Enter valid amount")
            time.sleep(1)
            return
        
        category = input("Enter the category: food/travel/clothes/other\n")
        if category not in ["food", "travel", "clothes", "other"]:
            print("Enter valid category")
            time.sleep(1)
            return

        description = input("Enter the description: \n")

        expenses.append({"Amount": amount,
                         "Category": category,
                         "Description": description})
        print("Added Successfully")

    elif choice == "2":
        print("--------------")
        for expense in expenses:
            print("--------------")
            print(f"Amount: {expense['Amount']}")
            print(f"Category: {expense['Category']}")
            print(f"Description: {expense['Description']}")
        print("--------------")
        
    else:
        print("Invalid Command")

def main():
    load()
    while running:
        menu()

main()