contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}"

def change_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} updated to {phone}"
    else:
        raise IndexError

def get_phone(name):
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}"
    else:
        raise IndexError

def show_all_contacts():
    if not contacts:
        return "No contacts available"
    else:
        result = "Contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()

def parser(command):
    if command.startswith("add"):
        _, name, phone = command.split(" ", 2)
        return add_contact(name, phone)
    elif command.startswith("change"):
        _, name, phone = command.split(" ", 2)
        return change_contact(name, phone)
    elif command.startswith("phone"):
        _, name = command.split(" ", 1)
        return get_phone(name)
    elif command == "all":
        return show_all_contacts()
    elif command == "hello":
        return "How can I help you?"
    else:
        return "Invalid command. Try again."    

def main():
    print("Hello i am your personal assistant")
    while True:
        command = input("Enter a command >>> ").lower()
        if command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print(parser(command))

if __name__ == "__main__":
    main()
