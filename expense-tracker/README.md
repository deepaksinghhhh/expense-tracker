# 💰 Expense Tracker

A command-line expense tracking application built with Python and MySQL.

## Features
- Add expenses with category, amount and description
- View all expenses in a table format
- View total spending
- Delete expenses
- Data stored permanently in MySQL database

## Tech Stack
- Python 3
- MySQL
- mysql-connector-python

## Database Setup
Run these commands in MySQL:
```sql
CREATE DATABASE expense_db;
USE expense_db;
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50),
    amount DECIMAL(10,2),
    description VARCHAR(100),
    date DATE
);
```

## How to Run
1. Install dependency:
   pip3 install mysql-connector-python
2. Setup database (see above)
3. Run:
   python3 expense.py

## Author
Deepak Singh | BCA Student | Chandigarh