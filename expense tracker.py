#expense tracker
import matplotlib.pyplot as plt

def show_menu():
    print("Expense Tracker")
    print("1. Add an Expense")
    print("2. View Summary")
    print("3. Delete an Expense")
    print("4. Exit")



def visualize_expenses_by_category(category_expenses):
    # Create a pie chart to represent expense distribution by category
    labels = category_expenses.keys()
    values = category_expenses.values()

    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title('Expense Distribution by Category')
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
    plt.show()


expenses = []  # Initialize as an empty list

def add_expense(expenses):
    print("\nAdd an Expense")
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category: ")
    date = input("Enter the date (YYYY-MM-DD): ")
     # Create an expense dictionary and append it to expenses
    expense = {"amount": amount, "category": category, "date": date}
    expenses.append(expense)
    print("Expense added successfully!")  

def calculate_total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

def calculate_expenses_by_category(expenses):
    category_expenses = {}
    for expense in expenses:
        category = expense["category"]
        if category in category_expenses:
            category_expenses[category] += expense["amount"]
        else:
            category_expenses[category] = expense["amount"]
    
    return category_expenses

def view_summary(expenses):
    print("\nExpense Summary")
    total_expenses = calculate_total_expenses(expenses)
    print(f"Total expenses: ${total_expenses}")

    # Example of calculating category-wise expenses (you can enhance this)
    category_expenses = {}
    for expense in expenses:
        category = expense["category"]
        if category in category_expenses:
            category_expenses[category] += expense["amount"]
        else:
            category_expenses[category] = expense["amount"]

    print("\nCategory-wise expenses:")
    for category, amount in category_expenses.items():
        print(f"{category}: ${amount}")  

def delete_expense(expenses):
    print("\nDelete an Expense")
    # Show expenses for selection (indexes or IDs) and get user input
    for index, expense in enumerate(expenses):
        print(f"{index + 1}. {expense['category']} - ${expense['amount']} - {expense['date']}")

    try:
        index_to_delete = int(input("Enter the expense number to delete: ")) - 1
        if 0 <= index_to_delete < len(expenses):
            del expenses[index_to_delete]
            print("Expense deleted successfully!")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_expense(expenses)  # Call function to add an expense
            pass  # Placeholder for the function
        elif choice == '2':
            view_summary(expenses)# Call function to view summary
            pass  # Placeholder for the function
        elif choice == '3':
            delete_expense(expenses)# Call function to delete an expense
            pass  # Placeholder for the function
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
