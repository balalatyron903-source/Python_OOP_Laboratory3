class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print("Vehicle is starting.")


class Car(Vehicle):
    def start(self):
        print("Car engine is starting.")


vehicle = Vehicle("Toyota", 100)
car = Car("Honda", 120)

vehicle.start()
car.start()