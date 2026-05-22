import mysql.connector
from datetime import date

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="expense_db"
)
cursor = conn.cursor()

def add_expense():
    category = input("Category (Food/Transport/Shopping/Other): ")
    amount = float(input("Amount (Rs): "))
    description = input("Description: ")
    today = date.today()
    
    cursor.execute("INSERT INTO expenses (category, amount, description, date) VALUES (%s, %s, %s, %s)",
                   (category, amount, description, today))
    conn.commit()
    print("✅ Expense added successfully!")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    
    if len(rows) == 0:
        print("No expenses found!")
        return
    
    print("\n--- All Expenses ---")
    print(f"{'ID':<5} {'Category':<15} {'Amount':<10} {'Description':<20} {'Date'}")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<15} Rs{row[2]:<9} {row[3]:<20} {row[4]}")

def view_total():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    if total:
        print(f"\n💰 Total Expenses: Rs {total}")
    else:
        print("No expenses yet!")

def delete_expense():
    view_expenses()
    id = int(input("\nKaunsa expense delete karna hai? (ID daalo): "))
    cursor.execute("DELETE FROM expenses WHERE id = %s", (id,))
    conn.commit()
    print("🗑️ Expense deleted!")

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total")
    print("4. Delete Expense")
    print("5. Exit")
    
    choice = input("Choose (1-5): ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_total()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice!")