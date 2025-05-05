### OOP Principles ###

from item import Item
from phone import Phone
from keyboard import Keyboard

### 1. Encapsulation ###
item1 = Item("MyItem", 750)

item1.apply_increment(0.2)
item1.apply_discount()

print(item1.price)


### 2. Abstraction ###
# Hiding unnecessary info to users

item2 = Item("MyItem", 750, 6)
item2.send_email()


### 3. Inheritance ###
# Reuse codes among classes
item3 = Phone("MyPhone", 1000, 3)
item3.apply_increment(0.2)

print(item3.price)


### 4. Polymorphism ###
# many forms
name = "Sunny"
print(len(name))

some_list = ["some", "list"]
print(len(some_list))

# That's polymorphismin in action, a single function/entity does know
# how to handle different kinds of objects as expected.

item4 = Keyboard("MyKeyboard", 1000, 3)
item4.apply_discount()
print(item4.price)
