class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_year(self):
        return self.year


class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def get_doors(self):
        return self.doors


class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine):
        super().__init__(brand, year)
        self.engine = engine

    def ride(self):
        print(self.brand, "motorcycle is moving.")


car = Car("Toyota", 2022, 4)
motorcycle = Motorcycle("Honda", 2024, 250)

print("Car Brand:", car.brand)
print("Car Year:", car.get_year())
print("Number of Doors:", car.get_doors())
print("Motorcycle Brand:", motorcycle.brand)
print("Motorcycle Year:", motorcycle.get_year())
print("Engine:", motorcycle.engine, "cc")
motorcycle.ride()
