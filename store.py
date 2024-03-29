class Product:
    def __init__(self, product_name, product_price, product_category):
        self.name = product_name
        self.price = product_price
        self.category = product_category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price + (self.price * percent_change)
        else:
            self.price = self.price - (self.price * percent_change)
        return self
    
    def print_info(self):
        print("Product name: ", self.name, "Category: ", self.category, "Price: ", self.price)
        return self


class Store:
    def __init__(self, store_name):
        self.name = store_name
        self.product_list = []
                    
    def add_product(self, new_product):
        self.product_list.append(new_product)
        return self
    
    def sell_product(self, id):
        print(self.product_list[id])
        del self.product_list[id]
        return self
        # or could write it like this:
        # sold_product = self.products.pop(id)
        # sold_product.print_info()
        # return self
    
    def inflation(self, percent_increase):
        for i in range(len(self.product_list)):
            self.product_list[i].update_price(percent_increase, True)
            return self
        # or could write it like this:
        # for product in self.product_list:
        #   product.update_price(percent_increase, True)
        # return self
    
    def set_clearance(self, category, percent_discount):
        for i in range(len(self.product_list)):
            if self.product_list[i].category == category:
                self.product_list[i].update_price(percent_discount, False)
                return self
        # or could write it like this:
        # for product in self.product_list:
        #   product.update_price(percent_discount, False)
        # return self

    def show_products(self):
        for product in self.product_list:
            product.print_info()
        return self


aldi = Store("aldi")

sour_cream_chips = Product("sour_cream_chips", 2, "snacks")
mild_salsa = Product("mild_salsa", 3, "snacks")
frozen_chicken = Product("frozen_chicken", 6, "frozen")
glazed_donuts = Product("glazed_donuts", 4, "bakedGoods")

aldi.add_product(sour_cream_chips).add_product(mild_salsa).add_product(frozen_chicken).add_product(glazed_donuts)

print(aldi.product_list)

mild_salsa.print_info()

aldi.inflation(1)

mild_salsa.print_info()

aldi.set_clearance("frozen", .25)

mild_salsa.print_info()

frozen_chicken.print_info()

aldi.sell_product(0)

aldi.show_products()