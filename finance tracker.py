import csv
from datetime import datetime

FILE_NAME = "finance_tracker.csv"

def initialize_file():
    try:
        with open(FILE_NAME, mode="x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount", "Description"])
    except FileExistsError:
        pass  

def add_entry(entry_type, category, amount, description):
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), entry_type, category, amount, description])
    print("Entry added successfully!")

def view_summary():
    try:
        income = 0
        expenses = 0
        with open(FILE_NAME, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Type"] == "Income":
                    income += float(row["Amount"])
                elif row["Type"] == "Expense":
                    expenses += float(row["Amount"])
        print("\n=== Finance Summary ===")
        print(f"Total Income: ${income:.2f}")
        print(f"Total Expenses: ${expenses:.2f}")
        print(f"Net Balance: ${income - expenses:.2f}")
        print("=======================\n")
    except FileNotFoundError:
        print("No records found. Start adding some entries first!")

def main():
    initialize_file()
    while True:
        print("=== Personal Finance Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            category = input("Enter income category (e.g., Salary, Investments): ")
            amount = float(input("Enter income amount: $"))
            description = input("Enter a description (optional): ")
            add_entry("Income", category, amount, description)
        elif choice == "2":
            category = input("Enter expense category (e.g., Food, Rent): ")
            amount = float(input("Enter expense amount: $"))
            description = input("Enter a description (optional): ")
            add_entry("Expense", category, amount, description)
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("Done with your details. ")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
    