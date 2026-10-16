inventory = []

def display_menu():
    """Display the available inventory management actions."""
    print("Inventory Management System")
    print("1. View Inventory")
    print("2. Add an item")
    print("3. Update an item quantity")
    print("4. Remove an item")
    print("5. Search inventory")
    print("6. View inventory summary")
    print("7. Exit")
    
def load_inventory(filename):
    """Load inventory data from a file into the inventory list."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, category, quantity = line.strip().split('|')
                inventory.append({"name": name, "category": category, "quantity": int(quantity)})
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty inventory.")
    except Exception as e:
        print(f"An error occurred while loading the inventory: {e}")
        
def save_inventory(inventory,filename):
    """Save the current inventory data to a file."""
    with open(filename, 'w') as file:
        for item in inventory:
            file.write(f"{item['name']}|{item['category']}|{item['quantity']}\n")

def view_inventory():
    """Display the current inventory items."""
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    for item in inventory:
        print(f"Name: {item['name']}, Category: {item['category']}, Quantity: {item['quantity']}")

def add_item():
    """Add a new item to the inventory."""
    try:
        name = input("Enter item name: ")
        category = input("Enter item category: ")
        quantity = int(input("Enter item quantity: "))
        inventory.append({"name": name, "category": category, "quantity": quantity})
        print(f"Item '{name}' added to inventory.")
        save_inventory(inventory, "inventory.txt")
    except ValueError:
        print("Invalid input. Quantity must be an integer.")

def update_item_quantity():
    """Update the quantity of an existing item in the inventory."""
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item['name']} | {item['category']} | Quantity: {item['quantity']}")

    try:
        item_number = int(input("Enter the item number to update: "))

        if item_number < 1 or item_number > len(inventory):
            print("Invalid item number.")
            return

        new_quantity = int(input("Enter the new quantity: "))

        if new_quantity < 0:
            print("Quantity cannot be negative.")
            return

        item = inventory[item_number - 1]
        item['quantity'] = new_quantity

        print(f"{item['name']} quantity updated to {new_quantity}.")

        save_inventory(inventory, "inventory.txt")

    except ValueError:
        print("Invalid input. Please enter a number.")

def remove_item():
    """Remove an item from the inventory."""
    name = input("Enter the name of the item to remove: ")
    for item in inventory:
        if item['name'].lower() == name.lower():
            inventory.remove(item)
            print(f"Item '{name}' removed from inventory.")
            save_inventory(inventory, "inventory.txt")
            return
    print(f"Item '{name}' not found in inventory.")    

def search_inventory():
    """Search for an item in the inventory by name."""
    name = input("Enter the name of the item to search: ")
    found_items = []
    for item in inventory:
        if name.lower() in item['name'].lower():
            found_items.append(item)
    if found_items:
        print("Search Results:")
        for item in found_items:
            print(f"Name: {item['name']}, Category: {item['category']}, Quantity: {item['quantity']}")
    else:
        print(f"No items found matching '{name}'.")

def main():
    """Main function to run the inventory management system."""
    print("Welcome to the Inventory Management System!")
    load_inventory("inventory.txt")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            view_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            update_item_quantity()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            search_inventory()
        elif choice == '6':
            view_inventory_summary()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")    
            
if __name__ == "__main__":
    main()