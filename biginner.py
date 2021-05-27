#  variables are decleared without types
import random
x = 4
name = 'Sally'

# variables can change types even after been set to a value
x = 'Sally'
print(x)  # the result is sally. changed from x to sally.

# casting . this is how to simply specify data type
x = str(5)
y = int(7)
z = float(3)

# to get the type of a variable we use the type() function

print(type(x), type(y), type(z))


# case sensitivity of variable names A won't overwrite a
a = 20
A = 'Jonny'

print(A, a)

# variable name must start with an alphabet or an _underscore no a space or hyphen is not allowed in variable name
myName = 'Lucas'
_myName = 'Lucas'
my_Name = 'Lucas'
MyNAME = 'Lucas'

# python allows for multiple variable assignment in one line.
x, y, z = 'orange', 'Mango', 'Cherry'
print(x, y, z)

# one value can be assigned to multiple variables in one line
x = y = z = 'Apple'
print(x, y, z)

# whe there is a collection of values in a list or tuple we can unpack them to a variable
cars = ["Benz", "Toyota", "Ford"]
x, y, z = cars
print(x, y, z)

# the addition sign is used for concatinating strings and variables. a number and a string cannot be combined.
print('I love ' + x, y, z)

# formatted strings can be used too
print(f'I love {x, y, z}')

# local and global variable
# to create a global variable in a function use the word global keyword


def start():
    global go
    go = 'begin'


start()
print('when you click start if ' + go)

# to change a global variable (decleared out side any function) inside a function use the global keyword
j = 'people'


def party():
    global j
    j = 'Family'


party()
print('The party is for the Entire ' + j)

# DATA TYPES IN PYTHON

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

# EXAMPLES OF THE TYPES
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	

"""
# complex numbers are written with a jas the imaginary part, complet numbers cant be converted into other numbers
x = 3+5j
y = 7j
z = 5j
print(type(x), type(y), type(z))

# to get a random number we have to import a built inn module called random
# this will display a single random number between 1 to 8
print(random.randrange(1, 8))

# to assign multiple string to a variable simply  use three double quotes
story = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(story,)

# square brackets can be used to get the position of a character in a string

greet = 'Hello World '
print(greet[1])

# strings as Arrays can be looped through
for x in greet:
    print(x)

# we use the len function to get the length of a string.
print(len(greet))

# to check if a phrase is present in a string we use the keyword in
txt = 'if you don"t like your life change it '
print('life' in txt)  # this will return a bool(True or False)

# we can implement this in an if or else statement.
if 'life' in txt:
    print('Yes, life is present ')

# to check if a phrase is  NOT present in a string we use the keyword in preceded by not
txt = 'if you don"t like your life change it '
print('life' not in txt)  # this will return a bool(True or False)

# we can implement this in an if or else statement.
if 'love' not in txt:
    print('Yes, love is  not present ')

# To slice a string we use the syntax that gets a positiona of a sting and a colon
greet = 'Hello world!'
# with 0 indexing this will slice from the 3rd letter to the 5th letter
print(greet[2:5])
# an empty space before the colon will start the slice from the beginning
print(greet[:5])
# an empty space after the colon will end the slice at the end
print(greet[4:])
# negative indexes start the slice from the end of the string
print(greet[-8:-3])

print()

# SOME STRING METHODS
# .upper()  this turns the string to uppercase
word = 'For the Lord, our God, wont let us down, he will bless us all'
print(word.upper())

print()

# .lower()  this turns the string to lowercase
word = 'For the Lord, our God, wont let us down, he will bless us all'
print(word.lower())

print()

# .replace()  this replaces an individual character, phrase or the entire string
word = 'For the Lord, our God, wont let us down, he will bless us all'
print(word.replace('Lord', 'Almighty'))

print()

# .strip()  this removes any white space in the beginning or end of the string
word = '   For the Lord, our God, wont let us down, he will bless us all     '
print(word.strip())

print()

# .split()  this method returns a list where the text between the specified separator becomes the list items
# this splits the string into substrings if it finds instances of the separator
word = 'For the Lord, our God, wont let us down, he will bless us all'
print(word.split(','))

# to combine strings and numbers we use the format() method , we place the {} placeholder where we want the numbers to appear
age = 36
txt= 'I am {} years old'
print(txt.format(age))
print()

# the format method take multiple arguments
quantity = 8
item_no = 167
price = 14.99
info = 'I want {} wrist watch with item no {} of {} pounds'
print(info.format(quantity, item_no, price))

print()
