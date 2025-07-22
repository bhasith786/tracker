import csv
from datetime import datetime

FILENAME = "expenses.csv"

def add_expense():
    amount = input("Enter amount: ₹")
    category = input("Enter category (Food, Transport, etc.): ")
    description = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD) [Press Enter for today]: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully.\n")


def view_expenses():
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            expenses = list(reader)
            if not expenses:
                print("No expenses found.\n")
                return
            print("\n Date       | Category    | Description    | Amount")
            print("-" * 50)
            for row in expenses:
                print(f"{row[0]:10} | {row[1]:10} | {row[2]:12} | ₹{row[3]}")
            print("\n")
    except FileNotFoundError:
        print("No expenses file found yet.\n")


def summary():
    total = 0
    category_total = {}
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                amount = float(row[3])
                total += amount
                category_total[row[1]] = category_total.get(row[1], 0) + amount
        print(f"\nTotal spent: ₹{total:.2f}")
        print("Category-wise breakdown:")
        for cat, amt in category_total.items():
            print(f"- {cat}: ₹{amt:.2f}")
        print("\n")
    except FileNotFoundError:
        print("No expenses found.\n")


def main():
    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summary()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
