"""This file should have our melon-type classes in it."""
class Watermelon(object):
    
    def __init__(self):
        qty = 0
        self.species = "Watermelon"
        self.color = "green"
        self.is_imported = False
        self.shape = "natural"
        self.seasons = ["Fall", "Summer"]
        self.get_price(qty)

    def get_price(self, qty):

        self.price = 5
        
        if self.is_imported == True:
            total_price = self.price * 1.5 * qty
        else:
            total_price = self.price * qty

        if self.shape != "natural":
            final_price = total_price * 2
        else:
            final_price = total_price

        if qty >= 3:
            discount_price = final_price * 0.75
        else:
            discount_price = final_price
        return discount_price






class Cantaloupe(object):
    def __init__(self):
        self.species = "Cantaloupe"
        self.color = "tan"
        self.is_imported = False
        self.shape = "natural"
        self.seasons = ["Spring", "Summer"]

class Casaba(object):
    def __init__(self):
        self.species = "Casaba"
        self.color = "green"
        self.is_imported = True
        self.shape = "natural"
        self.seasons = ["Spring", "Winter", "Fall", "Summer"]

class Sharlyn(object):
    def __init__(self):
        self.species = "Sharlyn"
        self.color = "tan"
        self.is_imported = True
        self.shape = "natural"
        self.seasons = ["Summer"]



