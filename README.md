<!-- readme-refresh 2026-11 -->
<div align="center">

# 💰 Finance Tracker

**A command-line income and expense log**

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />

</div>

## ✨ Highlights

- Log income and expenses
- Running summary
- Python standard library only

<!-- body -->
Here is a README file for the personal finance tracker project on GitHub:

***

# Personal Finance Tracker

This is a simple command-line personal finance tracker application written in Python. It allows users to record income and expenses, and provides a summary of their total income, expenses, and net balance.

## Features

- Add income entries with category, amount, and optional description
- Add expense entries with category, amount, and optional description
- View a finance summary showing total income, total expenses, and net balance
- Data is stored persistently in a CSV file

## Requirements

- Python 3.x

## Usage

1. Run the script:

```bash
python finance_tracker.py
```

2. Follow the on-screen menu options to:

- Add Income
- Add Expense
- View Summary
- Exit the program

3. Data is saved automatically to `finance_tracker.csv` in the script's directory.

## How It Works

- The script initializes a CSV file with headers if it doesn't already exist.
- Income and expense entries are appended to the CSV file with date, type, category, amount, and description.
- The summary option reads the CSV file and calculates total income, expenses, and net balance.
- The interface runs in a loop until the user chooses to exit.

## Example

```
=== Personal Finance Tracker ===
1. Add Income
2. Add Expense
3. View Summary
4. Exit
Choose an option (1-4): 1
Enter income category (e.g., Salary, Investments): Salary
Enter income amount: $5000
Enter a description (optional): October paycheck
Entry added successfully!
```

## License

This project is open-source under the MIT License.

***

This README introduces the project, usage, and implementation details clearly. Let me know if further customization is desired!Here is a README file tailored for your personal finance tracker project:

***

# Personal Finance Tracker

A simple command-line application to track personal income and expenses, providing summaries of financial activity stored in a CSV file.

## Features

- Add income entries by category, amount, and optional description
- Add expense entries similarly
- View a summary showing total income, total expenses, and net balance
- Persistent storage of data in `finance_tracker.csv`

## Requirements

- Python 3.x

## Installation

No external libraries needed beyond Python standard library.

## Usage

Run the script to start the tracker:

```bash
python finance_tracker.py
```

Select from the menu to add income, add expenses, view summary, or exit.

## Code Overview

- Initializes CSV file with headings if it doesn’t exist
- Appends entries with timestamp, type (Income/Expense), category, amount, and description
- Calculates financial summary by reading and summing entries from the CSV

## Example Interaction

```
=== Personal Finance Tracker ===
1. Add Income
2. Add Expense
3. View Summary
4. Exit
Choose an option (1-4): 3

=== Finance Summary ===
Total Income: $5000.00
Total Expenses: $1200.00
Net Balance: $3800.00
=======================
```

## License

This project is open-source under the MIT License.

***

This README clearly explains the purpose, usage, and functionality of your finance tracker script. Let me know if any additions are wanted!

---

<div align="center"><sub>Built by <a href="https://github.com/Mokshitsharma">Mokshit Sharma</a> · <a href="https://mokshitsharma27.vercel.app/">Portfolio</a> · <a href="https://www.linkedin.com/in/mokshit-sharma-75b5ab305">LinkedIn</a></sub></div>
