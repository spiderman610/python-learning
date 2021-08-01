

# structure of class

# if a function is inside the class it is called method
# instance/object method - methods which are related to instance of class
# static method - methods which are not related to class
# class method - methods which are related to class definition

class Animal:

	number_of_legs = 4  # class variable

	def __init__(self, name, food_type, teeth_size, has_horn):  # init method
		self.name = name  # instance variable
		self.food_type = food_type
		self.teeth_size = teeth_size
		self.has_horn = has_horn

	def is_the_animal_dangerous(self):
		if self.has_horn == True:
			return "dangerous"
		else:
			return "not dangerous"


dog = Animal(name="dog", teeth_size="big", food_type="non_veg", has_horn=False)
cow = Animal(name="cow", teeth_size="big", food_type="veg", has_horn=True)

print(cow.number_of_legs)
print(cow.food_type)
print(cow.is_the_animal_dangerous())
print(dog.number_of_legs)
print(dog.food_type)
print(dog.is_the_animal_dangerous())
