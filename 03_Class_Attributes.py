### Class Attributes ###

class Item:
    pay_rate = 0.8  # the pay rate after 20% discount --> class attribute
    all = []  # --> class attribute
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >=0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assign to self object
        self.name = name
        self.price = price 
        self.quantity = quantity

        # Actions to execute 
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity 
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate 

    def __repr__(self):  # magic method: representing your object
        return f"Item('{self.name}', {self.price}, {self.quantity})"



item1 = Item("Phone", 100, 1)

# Access to class attribute
print(Item.pay_rate)  # access to class attribute via class
print(item1.pay_rate) # access to class attribute via instance

# Access to all attributes
print(Item.__dict__)  # all the attributes for class level
print(item1.__dict__) # all the attributes for instance level

item1.apply_discount()
print(item1.price)  # --> 80


item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)  # --> 700


item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

for instance in Item.all:
    print(instance.name)

print(Item.all)




