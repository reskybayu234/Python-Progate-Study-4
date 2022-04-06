class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        if count >= 3:
          total_price *= 0.9
        # If count is 3 or higher, multiply it by 0.9
        return round(total_price)
        
        # Round total_price to the nearest whole number and return it
        
