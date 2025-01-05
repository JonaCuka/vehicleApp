from enum import Enum

class Vehicle:
    # TODO Vehicle implementation
	# TODO add attributes and Getters / Setters


    def __init__(self, id, manufacturer, model, horsePower, price, color, mileage, productionYear, transmission, fuelType ):
        self.__id = id
        self.__manufacturer = manufacturer
        self.__model = model
        self.__horsePower = horsePower
        self.__price = price
        self.__color = color
        self.__mileage = mileage
        self.__productionYear = productionYear
        self.__transmission = transmission
        self.__fuelType = fuelType

    def get_id(self):
        return self.__id
    def get_manufacturer(self):
        return self.__manufacturer
    def get_model(self):
        return self.__model    
    def get_horsePower(self):
        return self.__horsePower
    def get_price(self):
        return self.__price
    def get_color(self):
        return self.__color
    def get_mileage(self):
        return self.__mileage              
    def get_productYear(self):
        return self.__productionYear
    def get_transmission(self):
        return self.__transmission
    def get_fuelType(self):
        return self.__fuelType     


    def set_id(self, id):
        self.__id = id

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def set_model(self, model):
        self.__model = model

    def set_horsepower(self, horsePower):
        self.__horsePower = horsePower

    def set_price(self, price):
        self.__price = price

    def set_color(self, color):
        self.__color = color

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_year(self, productionYear):
        self.__productionYear = productionYear

    def set_fuel_type(self, fuelType ):
        self.__fuelType  = fuelType 

    def set_transmission(self, transmission):
        self.__transmission = transmission       

        
    

class Color(Enum):
    # TODO define color enumeraition literals 

    BLACK = 1
    GREY = 2
    WHITE  = 3
    BLUE = 4 
    RED = 5
    BROWN = 6
    YELLOW = 7

    

class FuelType(Enum):
    # TODO define fuel type enumeraition literals
    GASOLINE = 1
    DIESEL_FUEL = 2
    

class Manufacturer(Enum):
    # TODO define manufacturer enumeraition literals
    
    AUDI = 1
    BMW = 2
    VW  = 3
    HONDA = 4 
    SKODA = 5
    

class Transmission(Enum):
    # TODO define transmission enumeraition literals 
    AUTOMATIC = 1
    MANUAL = 2
    