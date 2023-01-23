# Creating a class and object :
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
dog1 = Dog("Tommy",2)
print("Name :",dog1.name )
print("Age:",dog1.age)

