# prepared import of enumerations
from model import Color, FuelType, Manufacturer, Transmission, Vehicle
# prepared csv module import
import csv
from typing import List


class VehicleFileManager:
    def __init__(self, file_path):
        self.file_path = file_path



    def import_vehicles_from_file(self, file_path):

        # TODO read vehicle-list.csv and transform to String array
        vehicle_list = []
        try:
            with open(self.file_path, mode='r') as file:
                reader = csv.reader(file)
                
                for row in reader:
                    vehicle_list.append(row)  
        except Exception as error:
            print("Error reading file:" + error)

        return vehicle_list
           

        

    def rewrite_file(self, vehicle_list):
        # TODO write back into vehicle-list.csv and transform to String array
	    # TODO call method prepare_the_vehicle_for_rewriting(String, Vehicle)

       
        try:
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                for vehicle in vehicle_list:
                    vehicle_string = self.prepare_the_vehicle_for_rewriting('', vehicle)
                    writer.writerow(vehicle_string.split(','))
        except Exception as error:
            print("Error reading file: " + error)    
                

    def prepare_the_vehicle_for_rewriting(self, vehicle_string_for_rewrite, vehicle):
        #  TODO add vehicle attribute information to vehicle_string_for_rewrite
		# Hint: vehicle_string_for_rewrite.join(String)

        
        vehicle_string_for_rewrite = ",".join([
            str(vehicle.get_id()),
            vehicle.get_manufacturer().name,
            vehicle.get_model(),
            str(vehicle.get_horsePower()),
            str(vehicle.get_price()),
            vehicle.get_color().name,
            str(vehicle.get_mileage()),
            str(vehicle.get_productYear()),
            vehicle.get_fuelType().name,
            vehicle.get_transmission().name
        ])
        return vehicle_string_for_rewrite


class VehicleShopPrinter:
    
    def print_available_vehicles(self, vehicle_list):
        # TODO Implement print available vehicles

        if vehicle_list:
            print("\nAvailable Vehicles:")
            for vehicle in vehicle_list:
                print("ID: " + str(vehicle.get_id()) + " Manufacturer: " + vehicle.get_manufacturer().name + " Model: " + vehicle.get_model() + " Price: " + str(vehicle.get_price()) + " USD")
        else:
            print("No available vehicles.")
            
    
    def print_vehicle_sold_message(self, vehicle_chosen_id):
        print("\nVehicle with ID", vehicle_chosen_id, "was sold.")
    
    def print_vehicle_id_to_sell_message(self):
        print("\n\n Please enter the number (ID) of the vehicle you want to sell: ")



class VehicleShopProcessor:

    # responsible to sell a specified vehicle by id

    def sell_vehicle(self, vehicle_list, selected_vehicle_id):
    # TODO selling a vehicle means to remove it from the available vehicle list
        
        for vehicle in vehicle_list:
            if vehicle.get_id() == selected_vehicle_id:
                vehicle_list.remove(vehicle)
                return vehicle
        return None

class VehicleTransformer:

    # transforms a data array into a {@link Vehicle} list 
	# @param vehicle data array
	# @return list of {@link Vehicle} objects

    def transform_data_as_string_array_to_vehicle_objects(self, vehicles_as_string_array: List[List[str]]) -> List[Vehicle]:
        # TODO take data from String list and transform to list of vehicle objects
        # TODO call method transformToVehicleObject
        # Hint: use for loop
        vehicle_objects = []
        for vehicle_data in vehicles_as_string_array:
            if not isinstance(vehicle_data, list):
                raise ValueError("Expected a list of strings, but got something else")
            vehicle_objects.append(self.transform_to_vehicle_object(vehicle_data))
        return vehicle_objects

    # transforms a vehicle data record as String into a {@link Vehicle} object
	# @param vehicle data record as String 
	# @return {@link Vehicle} object 
    
    def transform_to_vehicle_object(self, vehicle_as_string_array: str) -> Vehicle: 
        # TODO transform the vehicle as string into a vehicle object
        if isinstance(vehicle_as_string_array, list):
            vehicle_id = int(vehicle_as_string_array[0])
            manufacturer = self.get_manufacturer_from_string(vehicle_as_string_array[1])
            model = vehicle_as_string_array[2]
            horse_power = int(vehicle_as_string_array[3])
            price = float(vehicle_as_string_array[4])
            color = self.get_color_from_string(vehicle_as_string_array[5])
            mileage = int(vehicle_as_string_array[6])
            production_year = int(vehicle_as_string_array[7])
            fuel_type = self.get_fuel_type_from_string(vehicle_as_string_array[8])
            transmission = self.get_transmission_from_string(vehicle_as_string_array[9])

            # Create a new Vehicle object using the extracted data
            vehicle = Vehicle(vehicle_id, manufacturer, model, horse_power, price, color, mileage, production_year, transmission, fuel_type)
            return vehicle
        else:
            raise ValueError("Expected a list of strings but got a non-list type.")
    
    # Example for Enumeration processing to use for all other Enumerations
    def get_manufacturer_from_string(self, manufacturer_as_string):
        for manufacturer in Manufacturer:
            if manufacturer.name == manufacturer_as_string:
                return manufacturer
            
        raise ValueError("Manufacturer not supported: " + manufacturer_as_string)
    

    def get_color_from_string(self, color_as_string):
        for color in Color:
            if color.name == color_as_string:
                return color
        raise ValueError("Color not supported: " + color_as_string)

    def get_fuel_type_from_string(self, fuel_type_as_string):
        for fuel_type in FuelType:
            if fuel_type.name == fuel_type_as_string:
                return fuel_type
        raise ValueError("Fuel Type not supported: " + fuel_type_as_string)

    def get_transmission_from_string(self, transmission_as_string):
        for transmission in Transmission:
            if transmission.name == transmission_as_string:
                return transmission
        raise ValueError("Transmission not supported: " + transmission_as_string)

