class MenuItem:
    def info(self):
      print(self.name + ": $" + str(self.price))
        # Output in the format '____: $____'
        


menu_item1 = MenuItem()
menu_item1.name = 'Sandwich'
menu_item1.price = 5

menu_item1.info()

menu_item2 = MenuItem()
menu_item2.name = 'Chocolate Cake'
menu_item2.price = 4

menu_item2.info()
