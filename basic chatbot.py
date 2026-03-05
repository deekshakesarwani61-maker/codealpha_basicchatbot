# Stock Portfolio Tracker

portfolio = {}

def add_stock():
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter purchase price per stock: "))
    
    if name in portfolio:
        portfolio[name]["quantity"] += quantity
        portfolio[name]["price"] = price     
    else:
        portfolio[name] = {"quantity": quantity, "price": price}
    
    print(f"{name} added successfully!\n")
     

     
def view_portfolio():
    if not portfolio:
        print("Portfolio is empty.\n")   
        return
    
    print("\n--- Your Portfolio ---")
    total_value = 0
    
    for stock, data in portfolio.items():
        quantity = data["quantity"]
        price = data["price"]       
        value = quantity * price
        total_value += value
        
        print(f"{stock} - Qty: {quantity}, Price: {price}, Value: {value}")
    
    print(f"Total Investment Value: {total_value}\n")    


def update_price():
    name = input("Enter stock name to update: ").upper()
    
    if name in portfolio:
        new_price = float(input("Enter new price: "))
        portfolio[name]["price"] = new_price
        print(f"{name} price updated!\n")
    else:
        print("Stock not found.\n")


def delete_stock():
    name = input("Enter stock name to delete: ").upper()
    
    if name in portfolio:
        del portfolio[name]
        print(f"{name} removed from portfolio.\n")
    else:
        print("Stock not found.\n")


def menu():
    while True:
        print("===== STOCK PORTFOLIO TRACKER =====")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Update Stock Price")
        print("4. Delete Stock")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            update_price()
        elif choice == "4":
            delete_stock()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")


# Run the program
menu()