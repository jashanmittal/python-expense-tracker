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
    print("1. Add expense\n2. View expense\n3. Total Expenses\n4. Category Expense\n5. Remove Expense\n6. Exit")
    choice = input()

    if choice == "6":
        save()
        exit()


    elif choice == "5":
        for index, expense in enumerate(expenses, start=1):
            print(f"""{index}.
                  Amount = {expense["Amount"]}
                  Category = {expense["Category"]}
                  Description = {expense["Description"]})
                  --------------------------------------------""")
            
        delete_choice = int(input("Which expense would you like to delete?\n"))
        expenses.pop(delete_choice - 1)



    elif choice == "4":
        print("Which category would you like to check:")
        print("1. Food\n2. Travel\n3. Clothes\n4. Other")
        select_category = input()

        category_map = {"1": "food",
                        "2": "travel",
                        "3": "clothes",
                        "4": "other"}
        
        if select_category not in category_map:
            print("Invalid Choice")
            return
        
        category_name = category_map[select_category]

        category_expense = sum(expense["Amount"] for expense in expenses
                               if expense["Category"] == category_name)
        
        print(f"Total {category_name} expenses are: {category_expense}")


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
