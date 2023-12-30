class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        return [(contact.name, contact.phone) for contact in self.contacts]

    def search_contact(self, search_query):
        results = []
        for contact in self.contacts:
            if (search_query in contact.name) or (search_query in contact.phone):
                results.append((contact.name, contact.phone))
        return results

    def update_contact(self, old_contact, new_contact):
        if old_contact in self.contacts:
            index = self.contacts.index(old_contact)
            self.contacts[index] = new_contact

    def delete_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)

if __name__ == "__main__":
    contact_manager = ContactManager()

    
    contact1 = Contact("John Doe", "1234567890", "john@example.com", "123 Main St")
    contact2 = Contact("Alice Smith", "9876543210", "alice@example.com", "456 Oak Ave")
    contact_manager.add_contact(contact1)
    contact_manager.add_contact(contact2)

    print("All Contacts:")
    all_contacts = contact_manager.view_contacts()
    for contact in all_contacts:
        print(contact)


    search_results = contact_manager.search_contact("John")
    print("Search Results:")
    for result in search_results:
        print(result)

    
    new_contact = Contact("John Doe", "9999999999", "john@example.com", "789 Elm St")
    contact_manager.update_contact(contact1, new_contact)

    
    contact_manager.delete_contact(contact2)

    
