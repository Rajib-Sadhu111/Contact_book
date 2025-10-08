# empty dictionary
contacts = {}

while True:
    print("\nContact Book App")
    print("1. Create contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contact")
    print("7. Exit")

    choice = input("enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        if name in contacts:
            print("contact name", name, "already exists")
        else:
            age = input("enter age: ")
            email = input("enter email: ")
            mobile = input("enter mobile number: ")
            contacts[name] = {"age":int(age), "email" : email, "mobile" : int(mobile)}
            print(f"Contact name {name} has been created successfully")

    elif choice == "2":
        name = input("enter contact name to view: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name:{name}, Age:{age}, Mobile number: {mobile}")
        else:
            print("Contact not found")

    elif choice == "3":
        name = input("enter name to update: ")
        if name in contacts:
            age = input("enter age: ")
            email = input("enter email: ")
            mobile = input("enter mobile number: ")
            contact[name] = {"age":int(age), "email" : email, "mobile" : int(mobile)}
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("enter name which you want to delete: ")
        if name in contacts:
            del contacts[name]
            print("delete contact successfully")
        else:
            print("Contact not found")

    elif choice == "5":
        search_name = input("enter name to search: ")
        found = False
        for name in contacts.items():
            if search_name.lower():
                print(f"Found - Name {name}, Age:{age}, Mobile number:{mobile}, Email:{email}")
                found = True
        if not found:
            print("No contact found with that name")
        
    elif choice == "6":
        print("Total contacts in your book:", len(contacts))

    elif choice == "7":
        print("Good Bye...Closing the Program")
        break

    else:
        print("Invalid input")

