In this video, we'll explore the fundamentals of OOP with Python. So, let's dive right in!

OOP is a programming paradigm that revolves around the concept of objects. Objects are the building blocks of OOP, and they allow us to organize our code in a logical and efficient manner. Imagine objects as real-world entities that have certain characteristics and behaviors. For example, a car object can have characteristics like color, model, and speed, while behaviors can include starting the engine or accelerating. OOP enables us to model these real-world concepts directly in our code. 

In Python, we use classes to create objects. A class is like a blueprint or a template that defines the structure and behavior of an object. It encapsulates data and functions into a single unit, making our code more organized and reusable.

Within a class, we define attributes, which are variables that hold data, and methods, which are functions that define the behavior of the object. These attributes and methods can be accessed and utilized by objects created from the class.

```python
class Car:
    def __init__(self, name, color):
        self.name = name # Your object characteristic (attribute)
        self.color = color

    def startEngine(self): # Your object behavior (method)
        print("Engine started")

    def accelerate(self): # Your object behavior (method)
        for i in range(3):
            print("Accelerating...")

```

One of the powerful aspects of OOP is the ability to model relationships between objects. Objects can interact with each other by invoking methods and exchanging data. This allows us to build complex systems and solve real-world problems more effectively. 

```python
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

if __name__ == "__main__":
    human = Human("John", 20, Car("BMW", "Black"))
    print(human.carName()) # BMW
```

Another important concept in OOP is inheritance. With inheritance, we can create a new class, known as a subclass, that inherits attributes and methods from an existing class, called the superclass or base class. This promotes code reuse and allows us to build upon existing functionality.

```python
class Teenager(Human): # Inherit from Human class
    def __init__(self, name, age, car):
        super().__init__(name, age, car) # Initialize your base class
        self.isGraduated = False # New attribute

    def drive(self, car: Car):
        if self.age < 18:
            print("You are not allowed to drive")
        else:
            super().drive(car)

if __name__ == "__main__":
    teen = Teenager("John", 17, Car("BMW", "Black"))
    print(teen.name)
    teen.drive()
```

Encapsulation is yet another key principle of OOP. It involves bundling data and methods within a class, and controlling access to them. This promotes data integrity and provides a clean interface for interacting with objects. We can use access modifiers like public, private, and protected to define the visibility and accessibility of class members.

Public access in Python means that the attribute or method is intended to be accessible and modifiable from outside the class

Private access in Python means that the attribute or method is intended for internal use within the class itself and should not be accessed or modified directly from outside the class

Protected access in Python means that the attribute or method is intended for internal use within the class itself and its subclasses. It signals to other developers that they should not access or modify the attribute or method directly from outside the class hierarchy. However, in reality, there is no technical restriction preventing access to these members from outside the class.

```python
class Teenager(Human):
    def __init__(self, name, age, car):
        super().__init__(name, age, car)
        self._isGraduated = False # New attribute (protected attribute)
        
    def drive(self):
        if self.age < 18:
            print("You are not allowed to drive")
        else:
            super().drive(self.car)
            
    def __graduate(self):
        self._isGraduated = True

if __name__ == "__main__":
    teen = Teenager("John", 17, Car("BMW", "Black"))
    print(teen.name) # John
    teen.drive()
    print(teen._name) # John Doe
    print(teen.__graduate()) # Not accessible
```

Lastly, OOP introduces polymorphism, which means 'many forms.' Through method overriding and method overloading, we can write code that can work with objects of different types in a uniform way. Polymorphism can also be achieved through method overloading in other programming languages. However, in Python, method overloading is not directly supported due to its dynamic nature. Instead, we can use default values or variable-length argument lists to achieve similar functionality.

```python
class Human:
    def __init__(self, name, age, car):
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
        self._isGraduated = False # New attribute

	# Method overriding, method overloading using default parameter
    def drive(self, car: Car = Car("Toyota", "Blue")):
        if self.age < 18:
            print("You are not allowed to drive")
        else:
            super().drive(self.car)
            
    def __graduate(self):
        self._isGraduated = True

if __name__ == "__main__":
    teen = Teenager("John", 17, Car("BMW", "Black"))
    human = Human("John", 20, Car("BMW", "Black"))
    teen.drive() # You are not allowed to drive
    human.drive() # Engine started, Accelerating...
```

Now that we've covered the basics of OOP in Python.