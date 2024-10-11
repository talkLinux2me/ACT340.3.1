stringy = "Everything is an Object in Python!!!"
print(stringy)
print(stringy.upper())
print(stringy.lower())
print(stringy.capitalize())

first_name= "john"
last_name= "doe"
full_name= f"{first_name} {last_name}"

print(full_name)

print(f"Hello, {full_name.title()}")

phrase= " reindeer games "

print(phrase.rstrip())
print(phrase.lstrip())
print(phrase.strip())

Famous = "Valerie"

Quote = "Patience, young grasshopper"

print(f'{Famous} once said, "{Quote}."')
print("{} once said, '{}.'".format(Famous,Quote))

course= "Per Scholas"

print(course[1])
print(course[3])
print(course[-5])

string1= "Slicing strings is easy!"

print(string1[:3])
print(string1[1: 6: 2])
print(string1[-1: -8: -2])
print(string1[: : -1])

