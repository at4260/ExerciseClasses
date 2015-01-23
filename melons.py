"""This file should have our melon-type classes in it."""
class Watermelon(object):
    
    def __init__(self):
        self.species = "Watermelon"
        self.color = "green"
        self.is_imported = False
        self.shape = "natural"
        self.seasons = ["Fall", "Summer"]
        self.price = 5

    def get_price(self, qty):
        price = self.price
        if self.is_imported == True:
            total_price = price * 1.5 * qty
        else:
            total_price = price * qty
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
        self.price = 5

    def get_price(self, qty):
        price = self.price
        if self.is_imported == True:
            total_price = price * 1.5 * qty
        else:
            total_price = price * qty
        if self.shape != "natural":
            final_price = total_price * 2
        else:
            final_price = total_price
        if qty >= 5:
            discount_price = final_price * 0.5
        else:
            discount_price = final_price
        return discount_price

class Casaba(object):
    def __init__(self):
        self.species = "Casaba"
        self.color = "green"
        self.is_imported = True
        self.shape = "natural"
        self.seasons = ["Spring", "Winter", "Fall", "Summer"]
        self.price = 5

    def get_price(self, qty):
        price = self.price
        if self.is_imported == True:
            total_price = price * 1.5 * qty
        else:
            total_price = price * qty
        if self.shape != "natural":
            final_price = total_price * 2
        else:
            final_price = total_price
        return final_price


class Sharlyn(object):
    def __init__(self):
        self.species = "Sharlyn"
        self.color = "tan"
        self.is_imported = True
        self.shape = "natural"
        self.seasons = ["Summer"]
        self.price = 5

    def get_price(self, qty):
        price = self.price
        if self.is_imported == True:
            total_price = price * 1.5 * qty
        else:
            total_price = price * qty
        if self.shape != "natural":
            final_price = total_price * 2
        else:
            final_price = total_price
        return final_price

class SantaClaus(object):
    def __init__(self):
        self.species = "Santa Claus"
        self.color = "green"
        self.is_imported = True
        self.shape = "natural"
        self.seasons = ["Winter", "Spring"]
        self.price = 5

    def get_price(self, qty):
        price = self.price
        if self.is_imported == True:
            total_price = price * 1.5 * qty
        else:
            total_price = price * qty
        if self.shape != "natural":
            final_price = total_price * 2
        else:
            final_price = total_price
        return final_price

class Christmas(object):
    def __init__(self):
        self.species = "Christmas"
        self.color = "green"
        self.is_imported = False
        self.shape = "natural"
        self.seasons = ["Winter"]
        self.price = 5

    def get_price(self, qty):
        price = self.price
        if self.is_imported == True:
            total_price = price * 1.5 * qty
        else:
            total_price = price * qty
        if self.shape != "natural":
            final_price = total_price * 2
        else:
            final_price = total_price
        return final_price

class HornedMelon(object):
    def __init__(self):
        self.species = "Horned Melon"
        self.color = "yellow"
        self.is_imported = True
        self.shape = "natural"
        self.seasons = ["Summer"]
        self.price = 5

    def get_price(self, qty):
        price = self.price
        if self.is_imported == True:
            total_price = price * 1.5 * qty
        else:
            total_price = price * qty
        if self.shape != "natural":
            final_price = total_price * 2
        else:
            final_price = total_price
        return final_price

class Xigua(object):
    def __init__(self):
        self.species = "Xigua"
        self.color = "black"
        self.is_imported = True
        self.shape = "square"
        self.seasons = ["Summer"]
        self.price = 5

    def get_price(self, qty):
        price = self.price
        if self.is_imported == True:
            total_price = price * 1.5 * qty
        else:
            total_price = price * qty
        if self.shape != "natural":
            final_price = total_price * 2
        else:
            final_price = total_price
        return final_price

class Ogen(object):
    def __init__(self):
        self.species = "Ogen"
        self.color = "tan"
        self.is_imported = False
        self.shape = "natural"
        self.seasons = ["Spring", "Summer"]
        self.price = 5

    def get_price(self, qty):
        price = self.price
        if self.is_imported == True:
            total_price = price * 1.5 * qty
        else:
            total_price = price * qty
        if self.shape != "natural":
            final_price = total_price * 2
        else:
            final_price = total_price
        return final_price
