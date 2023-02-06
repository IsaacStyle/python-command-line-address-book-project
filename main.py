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
        print("Welcome to the greatest Address Book application the world has ever seen!")
        proceed = input("If you would like to continue, press 'y', if not, then press 'n'!\n")
        while proceed != 'y' and proceed != 'n':
           proceed = input(f"Apologies if you misread... {proceed} is not a valid response. Are you perhaps not educated? Press 'y' to continue, if not, then press 'n'.\n")
    print("Thank you for using our industry leading application!\nWe hope to see you again soon!")

address_book()  