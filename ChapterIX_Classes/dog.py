#Creating and Using a Class
# You can model almost anything using classes. Let's start by writing a simple class, Dog, that represents a dog. This class will tell Python how to make an object representing a dog. After our class is written, we'll use it to make individual instances, each of which represents one specific dog. 

# Creating the Dog Class
# Each instance created the Dog class will store a name and age, and we'll give each dog the ability to sit() and roll_over():
class Dog:
    def __init__(self,name,age): #Initialize name,age and attributes
        self.name = name
        self.age = age

    def sit(self): #Simulate a dog sitting in response to a command.
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

# The __init__() Method
# A function that's part of a class is a method. Everything you learned about functions applies to methods as well. 

# Making an Instance from a Class
# Think of a class as a set of instructions for how to make an instance. The class Dog is a set of instructions that tells Python how to make individual instances representing specific dogs. 
my_dog = Dog("Biscuit", 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Accessing Attributes
# To access the attributes of an instance, you use dot notation.

# Calling Methods
# After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog. Let's make our dog sit and roll over:
my_dog.sit()
my_dog.roll_over()

#Creating Multiple Instances
# You can create as many instances from a class as you need. Lets create a second dog:
class Dog:
    def __init__(self,name,age): #Initialize name,age and attributes
        self.name = name
        self.age = age

    def sit(self): #Simulate a dog sitting in response to a command.
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('Biscuit', 3)
your_dog = Dog('Jackson', 6)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

