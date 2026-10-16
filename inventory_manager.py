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