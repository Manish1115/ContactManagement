import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from a JSON file."""
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_contacts(contacts):
    """Save contacts to a JSON file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    """Add a new contact."""
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    """View all contacts."""
    contacts = load_contacts()
    if not contacts:
        print("No contacts found!")
        return
    
    print("\nContacts List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")

def search_contact():
    """Search for a contact by name."""
    search_name = input("Enter name to search: ").lower()
    contacts = load_contacts()
    
    found_contacts = [c for c in contacts if search_name in c['name'].lower()]
    
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"{contact['name']} - {contact['phone']} - {contact['email']}")
    else:
        print("No matching contacts found.")

def delete_contact():
    """Delete a contact by name."""
    name_to_delete = input("Enter name to delete: ").lower()
    contacts = load_contacts()
    
    new_contacts = [c for c in contacts if c['name'].lower() != name_to_delete]
    
    if len(new_contacts) < len(contacts):
        save_contacts(new_contacts)
        print(f"Contact '{name_to_delete}' deleted successfully!")
    else:
        print("Contact not found!")

def main():
    while True:
        print("\n📞 Contact Management System 📞")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
