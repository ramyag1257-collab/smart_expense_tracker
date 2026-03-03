import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# -----------------------------
# Initialize CSV file
# -----------------------------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["date", "category", "amount", "description"])


# -----------------------------
# Add Expense
# -----------------------------
def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')

        category = input("Enter category (Food/Travel/Bills/Other): ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")

        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])

        print("✅ Expense added successfully!\n")

    except ValueError:
        print("❌ Invalid amount. Please enter a number.\n")


# -----------------------------
# View All Expenses
# -----------------------------
def view_expenses():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            next(reader) # skip header
            print("\n--- All Expenses ---")
            for row in reader:
                print(row)
            print()
    except FileNotFoundError:
        print("No expenses found.\n")


# -----------------------------
# Category Summary
# -----------------------------
def category_summary():
    summary = {}

    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["category"]
            amount = float(row["amount"])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    print("\n--- Category Summary ---")
    for category, total in summary.items():
        print(f"{category}: ₹{total}")
    print()


# -----------------------------
# Monthly Summary
# -----------------------------
def monthly_summary():
    summary = {}

    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            month = row["date"][:7] # YYYY-MM
            amount = float(row["amount"])

            if month in summary:
                summary[month] += amount
            else:
                summary[month] = amount

    print("\n--- Monthly Summary ---")
    for month, total in summary.items():
        print(f"{month}: ₹{total}")
    print()


# -----------------------------
# Main Menu
# -----------------------------
def main():
    initialize_file()

    while True:
        print("==== Smart Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category_summary()
        elif choice == '4':
            monthly_summary()
        elif choice == '5':
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
