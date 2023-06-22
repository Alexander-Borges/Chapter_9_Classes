# 1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called upon open_restaurant() that prints a message indicating that the restaurant is open. 
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods. 

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a good restaurant to go to if you enjoy {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Puesto","Mexican")

print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()








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
your_dog.sit()