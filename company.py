#Author: Jacob Peel
#Program Description: Company Class

#Create Company class
class Company:

    #Define __init__ method
    def __init__(self, new_id, new_name, new_quantity, new_price, new_unit_price):
        #Set attributes to values
        self.__id = new_id
        self.__name = new_name
        self.__quantity = int(new_quantity)
        self.__price = float(new_price)
        self.__unit_price = float(new_unit_price)

    #Define get_id method
    def get_id(self):
        return self.__id

    #Define get_name method
    def get_name(self):
        return self.__name

    #Define get_quantity method
    def get_quantity(self):
        return self.__quantity

    #Define get_price method
    def get_price(self):
        return self.__price

    #Define get_unitprice method
    def get_unit_price(self):
        return self.__unit_price

    #Define __str__ method
    def __str__(self):
        string = "{:<18}{:<8}{:<3}".format(self.__name, str(self.__quantity), "$" + str("{0:.2f}".format(self.__price)))
        return string
        
