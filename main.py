from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from docopt import docopt

db = PostgresqlDatabase('contacts', user='isaac', password='iamstan', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db


class Contact(BaseModel):
  firstName = CharField()
  lastName = CharField()
  number = CharField()
  altNumber = CharField()
  address = CharField()

db.connect()
db.drop_tables([Contact])
db.create_tables([Contact])

Contact(firstName = 'Beeg', lastName = 'Enlarge', number = '555-6969', altNumber = 'none', address = '123 Beeger Street').save()
Contact(firstName = 'Mike', lastName = 'Literus', number = '555-6970', altNumber = 'none', address = '123 Beegerer Street').save()
Contact(firstName = 'Ivanna', lastName = 'Tinkle', number = '555-6971', altNumber = 'none', address = '123 Beegererer Street').save()
Contact(firstName = 'Edward', lastName = 'Ligma', number = '555-6972', altNumber = 'none', address = '123 Beegerererer Street').save()
Contact(firstName = 'Deez', lastName = 'Samuels', number = '555-6973', altNumber = 'none', address = '123 smol street').save()


for i in Contact.select().where(Contact.firstName == 'Beeg'):
  print(i.firstName)


# docopt(beeg, argv=None, help=True, version=None, options_first=False)

# usage: beeg

def address_book():
    proceed = 'y'
    while proceed == 'y':
        all_contacts = ""
        one_contact = ""
        contact_name= ""
        create_contact = ""
        update_contact = ""
        delete_contact = ""
        idd = 0
        fname = ""
        lname = ""
        number = ""
        number2 = ""
        addresss = ""
        print("Welcome to the greatest Address Book application the world has ever seen!")
        proceed = input("\nIf you would like to continue, press 'y', if not, then press 'n'!\n")
        while proceed != 'y' and proceed != 'n':
           proceed = input(f"Apologies if you misread... {proceed} is not a valid response. Are you perhaps not educated? Press 'y' to continue, if not, then press 'n'.\n")
        if proceed == 'y':
            print("\nThank you for choosing to proceed!")
            all_contacts = input("\nWould you like to view all your contacts? Press 'y' f yes, if not, then press 'n'!\n")
            while all_contacts != 'y' and all_contacts != 'n':
                all_contacts = input(f"\nApologies if you misread... {all_contacts} is not a valid response. Are you perhaps not educated? Press 'y' to continue, if not, then press 'n'.\n")
            if all_contacts == 'y':
                for i in Contact:
                   print(f"\nContact ID: {i.id}")
                   print(f"First Name: {i.firstName}")
                   print(f"Last Name: {i.lastName}")
                   print(f"Number: {i.number}")
                   print(f"Alt number: {i.altNumber}")
                   print(f"Address: {i.address}\n")
            one_contact = input("Would you like to search for a contact by name? Press 'y' f yes, if not, then press 'n'!\n")
            while one_contact != 'y' and one_contact != 'n':
                one_contact = input(f"Apologies if you misread... {one_contact} is not a valid response. Are you perhaps not educated? Press 'y' to continue, if not, then press 'n'.\n")
            if one_contact == 'y':
               contact_name = input("\nWhat is the name of your contact?\n")
               for i in Contact.select().where(Contact.firstName == contact_name):
                   print(f"\nContact ID: {i.id}")
                   print(f"First Name: {i.firstName}")
                   print(f"Last Name: {i.lastName}")
                   print(f"Number: {i.number}")
                   print(f"Alt number: {i.altNumber}")
                   print(f"Address: {i.address}\n")
            create_contact = input("Would you like to create a contact? Press 'y' f yes, if not, then press 'n'!\n")
            while create_contact != 'y' and create_contact != 'n':
                create_contact = input(f"\nApologies if you misread... {create_contact} is not a valid response. Are you perhaps not educated? Press 'y' to continue, if not, then press 'n'.\n")
            if create_contact == 'y':
                fname = input("Input First Name\n")
                lname = input("Input Last Name\n")
                number = input("Input Number\n")
                number2 = input("Input Alternate Number\n")
                addresss = input("Input Address\n")
                Contact(firstName = fname, lastName = lname, number = number, altNumber = number2, address = addresss).save()
                for i in Contact.select().where(Contact.firstName == fname):
                   print("\nHere is your new contact info.")
                   print(f"\nContact ID: {i.id}")
                   print(f"First Name: {i.firstName}")
                   print(f"Last Name: {i.lastName}")
                   print(f"Number: {i.number}")
                   print(f"Alt number: {i.altNumber}")
                   print(f"Address: {i.address}\n")
            update_contact = input("Would you like to edit a contact? Press 'y' f yes, if not, then press 'n'!\n")
            while update_contact != 'y' and update_contact != 'n':
                update_contact = input(f"\nApologies if you misread... {update_contact} is not a valid response. Are you perhaps not educated? Press 'y' to continue, if not, then press 'n'.\n")
            if update_contact == 'y':
                idd = input("What is your contact's id?\n")
                for i in Contact.select().where(Contact.id == idd):
                    print(f"\nContact ID: {i.id}")
                    print(f"First Name: {i.firstName}")
                    print(f"Last Name: {i.lastName}")
                    print(f"Number: {i.number}")
                    print(f"Alt number: {i.altNumber}")
                    print(f"Address: {i.address}\n")
                update_contact = input("Is this your contact? Press 'y' f yes, if not, then press 'n'!\n")
                while update_contact != 'y' and update_contact != 'n':
                    update_contact = input(f"\nApologies if you misread... {update_contact} is not a valid response. Are you perhaps not educated? Press 'y' to continue, if not, then press 'n'.\n")
                while update_contact == 'n':
                    idd = input("What is your contact's id?\n")
                    for i in Contact.select().where(Contact.id == idd):
                        print(f"\nContact ID: {i.id}")
                        print(f"First Name: {i.firstName}")
                        print(f"Last Name: {i.lastName}")
                        print(f"Number: {i.number}")
                        print(f"Alt number: {i.altNumber}")
                        print(f"Address: {i.address}\n")
                    update_contact = input("Is this your contact? Press 'y' f yes, if not, then press 'n'!\n")
                fname = input("Input First Name\n")
                lname = input("Input Last Name\n")
                number = input("Input Number\n")
                number2 = input("Input Alternate Number\n")
                addresss = input("Input Address\n")
                Contact.update(firstName = fname, lastName = lname, number = number, altNumber = number2, address = addresss).where(Contact.id == idd).execute()
                for i in Contact.select().where(Contact.id == idd):
                    print("\nHere is your updated contact info.")
                    print(f"\nContact ID: {i.id}")
                    print(f"First Name: {i.firstName}")
                    print(f"Last Name: {i.lastName}")
                    print(f"Number: {i.number}")
                    print(f"Alt number: {i.altNumber}")
                    print(f"Address: {i.address}\n")
            delete_contact = input("Would you like to delete a contact? Press 'y' f yes, if not, then press 'n'!\n")
            while delete_contact != 'y' and delete_contact != 'n':
                delete_contact = input(f"\nApologies if you misread... {delete_contact} is not a valid response. Are you perhaps not educated? Press 'y' to continue, if not, then press 'n'.\n")
            if delete_contact == 'y':
                idd = input("What is your contact's id?\n")
                for i in Contact.select().where(Contact.id == idd):
                    print(f"\nContact ID: {i.id}")
                    print(f"First Name: {i.firstName}")
                    print(f"Last Name: {i.lastName}")
                    print(f"Number: {i.number}")
                    print(f"Alt number: {i.altNumber}")
                    print(f"Address: {i.address}\n")
                delete_contact = input("Is this your contact? Press 'y' f yes, if not, then press 'n'!\n")
                while delete_contact != 'y' and delete_contact != 'n':
                    delete_contact = input(f"\nApologies if you misread... {delete_contact} is not a valid response. Are you perhaps not educated? Press 'y' to continue, if not, then press 'n'.\n")
                while delete_contact == 'n':
                    idd = input("What is your contact's id?\n")
                    for i in Contact.select().where(Contact.id == idd):
                        print(f"\nContact ID: {i.id}")
                        print(f"First Name: {i.firstName}")
                        print(f"Last Name: {i.lastName}")
                        print(f"Number: {i.number}")
                        print(f"Alt number: {i.altNumber}")
                        print(f"Address: {i.address}\n")
                    delete_contact = input("Is this your contact? Press 'y' f yes, if not, then press 'n'!\n")
                delete_contact = input(f"Are you sure you wish to delete contact {idd}? Press 'y' f yes, if not, then press 'n'!\n")
                while delete_contact != 'y' and delete_contact != 'n':
                    delete_contact = input(f"\nApologies if you misread... {delete_contact} is not a valid response. Are you perhaps not educated? Press 'y' to continue, if not, then press 'n'.\n")
                if delete_contact == 'y':
                    Contact.delete().where(Contact.id == idd).execute()
                    print(f"\nContact {idd} Deleted For All Eternity.")
            proceed = input("\nAll operations complete, would you like to go back to the top? Press 'y' f yes, if not, then press 'n'!\n")
            while proceed != 'y' and proceed != 'n':
                proceed = input(f"\nApologies if you misread... {proceed} is not a valid response. Are you perhaps not educated? Press 'y' to continue, if not, then press 'n'.\n")

    print("\nThank you for using our industry leading application!\nWe hope to see you again soon!")

address_book()  