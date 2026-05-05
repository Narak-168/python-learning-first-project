#This is the using of input function in Python Programming Language.
print("-------------------User Information------------------")
id = input("Enter your ID: ")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
nationality = input("Enter your nationality: ")

print("-----------------Show The Results-----------------")
print(f"The user's ID is {id} and his name is {name}. Currently, he is {age} years old and he is {nationality}. The type of id {type(id)} and the type of age {type(age)}.")