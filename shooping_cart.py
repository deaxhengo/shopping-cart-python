class Product:
    def __init__(self, name, price, quantity, discount=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount

    def total(self):
        total_price = self.price * self.quantity

        if self.discount > 0:
            total_price = total_price - (total_price * self.discount / 100)

        return total_price


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_price = 0
        self.discount = 0

    def add_to_cart(self, product):
        self.items.append(product)

    def remove_from_cart(self, product):
        if product in self.items:
            self.items.remove(product)

    def set_discount(self, discount):
        self.discount = discount

    def calculate_total(self):
        total = 0
        for product in self.items:
            total += product.total()
        if self.discount > 0:
            total = total - (total * self.discount / 100)
        self.total_price = total
        return total

    def show_products(self):
        print("SHOPPING CART:")

        for product in self.items:
            print("Product:", product.name)
            print("Quantity:", product.quantity)
            print("Price:", product.price, "€")
            print("Product discount:", product.discount, "%")
            print("Product total:", product.total(), "€")
        print("Cart discount:", self.discount, "%")
        print("Overall total:", self.calculate_total(), "€")

product1 = Product("T-shirt", 20, 2)
product2 = Product("Jeans", 50, 1, 10)
product3 = Product("Shoes", 80, 1, 20)

cart = ShoppingCart()

cart.add_to_cart(product1)
cart.add_to_cart(product2)
cart.add_to_cart(product3)

cart.set_discount(5)
cart.show_products()

class Product:
    def __init__(self, name:str, quantity:int, price:float, discount:float=None):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount

    def total_price(self):
        total = self.price*self.quantity
        if self.discount:
            total_price = total - self.discount*total
        else:
            total_price = total
        return total_price
product1 = Product(name="t-shirt", quantity=1, price=100, discount=0.1)
product2 = Product(name="pants", quantity=1, price=200)
print(product1.total_price())
print(product2.total_price())
total = product1.total_price() + product2.total_price()
print(total)

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_price = 0
        self.discount = None

    def add_to_cart(self, product):
        self.items.append(product)

    def remove_from_cart(self, product):
        if product in self.items:
            self.items.remove(product)

    def set_discount(self, discount):
        if discount >1:
            print("Discount can not be greater than 1")
            if discount<=0:
                print("Discount can not be less than 0")
        self.discount = discount
    def calculate_total(self):
        total = 0
        for product in self.items:
            total += product.total_price()
        if self.discount:
            total = total - self.discount * total
        self.total_price = total
        return total

    def show_products(self):
        print("Shopping Cart:")

        for product in self.items:
            print(
                product.name,
                "quantity:", product.quantity,
                "total price:", product.total_price()
            )
        print("Cart discount:", self.discount)
        print("Overall total:", self.calculate_total())

cart = ShoppingCart()

cart.add_to_cart(product1)
cart.add_to_cart(product2)

cart.set_discount(0.05)
cart.show_products()
