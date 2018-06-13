from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create user
User1 = User(name="sriku", email="charla.srikanth@gmail.com")
             
session.add(User1)
session.commit()

# Menu for Desserts
restaurant1 = Restaurant(user_id=1, name="Desserts")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Vanilla", description="A mixture made of cream, sugar, and vanilla.",
                     price="Rs.20", course="Ice-cream", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Strawberry", description="Strawberry flavoring with the cream and sugar.",
                     price="Rs.20", course="Ice-cream", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chocolate", description="Blending cocoa powder with the cream and sugar.",
                     price="Rs.50", course="Ice-cream", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Black current", description="Blending grapes along with the cream and sugar.",
                     price="Rs.70", course="Ice-cream", restaurant=restaurant1)

session.add(menuItem3)
session.commit()


# Menu for Milkshakes
restaurant2 = Restaurant(user_id=1, name="Milkshakes")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Vanilla milkshake", description="A blend of milk and fresh vanilla essence.",
                     price="RS.40", course="milkshakes", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Strawberry milkshake",
                     description="A blend of fresh strawberries and milk.", price="Rs.55", course="milkshakes", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Dryfruit milkshake", description="All healthy dryfruits with milk.",
                     price="Rs.85", course="milkshakes", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

# Menu for Thickshakes
restaurant1 = Restaurant(user_id=1, name="Thickshakes")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Dryfruit", description="A blend of dryfruits with thick icecream.",
                     price="Rs.100", course="thickshakes", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chocolate", description="ich chocolate blended with icecream.",
                     price="Rs.155", course="thickshakes", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Oreo", description="Chocolate milkshake with oreo flavour.",
                     price="Rs.150", course="thickshakes", restaurant=restaurant1)

session.add(menuItem3)
session.commit()


print "added menu items!"