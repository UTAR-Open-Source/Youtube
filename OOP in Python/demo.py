class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def startEngine(self):
        print("Engine started")

    def accelerate(self):
        for i in range(3):
            print("Accelerating...")

class Human:
    def __init__(self, name, age, car: Car):
        self.name = name
        self.age = age
        self.car = car
    
    def drive(self):
        self.car.startEngine()
        self.car.accelerate()

    def carName(self):
        return self.car.name

class Teenager(Human):
    def __init__(self, name, age, car):
        super().__init__(name, age, car)
        # Set protected attribute with single underscore
        self._isGraduated = False
    
    # Method overriding by owerwrite the parent method
    # method overloading using default parameter
    def drive(self, car: Car = Car("Toyota", "Blue")):
        if self.age < 18:
            print(f"You are not allowed to drive {car.name}")
        else:
            super().drive(self.car)
    
    # Set private method with double underscore
    def __graduate(self):
        self._isGraduated = True

if __name__ == "__main__":
    human = Human("John", 20, Car("BMW", "Black"))
    human.drive() # Engine started, Accelerating...
    print(human.carName()) # BMW

    teen = Teenager("John", 17, Car("BMW", "Black"))
    print(teen.name) # John
    print(teen.drive()) # You are not allowed to drive
    print(teen.__graduate()) # Not accessible