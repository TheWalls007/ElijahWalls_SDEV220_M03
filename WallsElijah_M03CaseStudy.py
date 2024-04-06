"""
Car Infomation Storer

Elijah Walls

Created 4/6/24

This program asks the user information about their car, stores it in a class, then
displays it back to the user.

Ver 1.0 updated 4/6/24
"""

class Vehicle:
    def __init__(self, vehicleType):
        # Initialize the Vehicle object with a vehicle type
        self.vehicleType = vehicleType

class Automobile(Vehicle):
    def __init__(self, vehicleType, year, make, model, doors, roof):
        # Initialize the Automobile object with additional attributes
        super().__init__(vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def displayInfo(self):
        # Display information about the automobile
        print("Vehicle type:", self.vehicleType)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)

def main():
    # Main function to collect user input and display car details
    print("Enter details for your car:")
    vehicleType = "car"
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sun roof): ")

    # Validate the number of doors
    while doors not in ['2', '4']:
        print("Invalid number of doors. Please enter either 2 or 4.")
        doors = input("Number of doors (2 or 4): ")

    # Validate the type of roof
    while roof.lower() not in ['solid', 'sun roof']:
        print("Invalid type of roof. Please enter either 'solid' or 'sun roof'.")
        roof = input("Type of roof (solid or sun roof): ")

    # Create an instance of Automobile with user-provided details
    car = Automobile(vehicleType, year, make, model, doors, roof)
    print("\nCar details:")
    car.displayInfo()

if __name__ == "__main__":
    main()

