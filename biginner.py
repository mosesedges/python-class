#  variables are decleared without types
import random
x = 4
name = 'Sally'

# variables can change types even after been set to a value
x = 'Sally'
print(x)  # the result is sally. changed from 4 to sally.

# casting . this is how to simply change data type
x = str(5)
y = int(7)
z = float(3)

# to get the type of a variable we use the type() function

print(type(x), type(y), type(z))


# case sensitivity of variable names A won't overwrite a
a = 20
A = 'Jonny'

print(A, a)

# variable name must start with an alphabet or an _underscore  a space or hyphen is not allowed in variable name
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

print('when you click start it ' + go)

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
# complex numbers are written with a j as the imaginary part, complex numbers cant be converted into other numbers
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

greet = 'Hello World'
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

# To slice a string we use the syntax that gets a positiona of a string and a colon
greet = 'Hello world!'
# with 0 indexing this will slice from the 2nd letter to the 7th letter
print(greet[2:8])
# an empty space before the colon will start the slice from the beginning
print(greet[:5])
# an empty space after the colon will end the slice at the end
print(greet[4:])
# negative indexes start the slice from the end of the string
print(greet[-8:-3])

print()

# SOME STRING METHODS
# .upper()  this turns the string to uppercase
word = 'For the Lord, our God, won\'t let us down, he will bless us all'
print(word.upper())

print()

# .lower()  this turns the string to lowercase
word = 'For the Lord, our God, won\'t let us down, he will bless us all'
print(word.lower())

print()

# .replace()  this replaces an individual character, phrase or the entire string
word = 'For the Lord, our God, won\'t let us down, he will bless us all'
print(word.replace('Lord', 'Almighty'))

print()

# .strip()  this removes any white space in the beginning or end of the string
word = '   For the Lord, our God, won\'t let us down, he will bless us all     '
print(word.strip())

print()

# .split()  this method returns a list where the text between the specified separator becomes the list items
# this splits the string into substrings if it finds instances of the separator
word = 'For the Lord, our God, won\'t let us down, he will bless us all'
print(word.split(','))

# to combine strings and numbers we use the format() method , we place the {} placeholder where we want the numbers to appear
age = 36
txt = 'I am {} years old'
print(txt.format(age))
print()

# the format method take multiple arguments
quantity = 8
item_no = 167
price = 14.99
info = 'I want {} wrist watch with item no {} of {} pounds'
print(info.format(quantity, item_no, price))

print()

# The format method can also take in 0 index numbers {0}to help affix each number apprioprately

weight = 80
height = 6.2
age = 14
info = 'He is aged {2} with height of {1} and weighs {0} pounds'
# by inputting the right index the variable can be formatted from haphazardly or serially
print(info.format(weight, height, age))
print()
# A backslash is an excape character in python, simply add the backslash before the escape character
print(' We are the so called  \'Gunners\'')

print()
print('Welcome \'home\'')  # \'	Single Quote
print('Welcome home \\')  # \\	Backslash
print('Welcome\n home')  # \n	New Line
print('Welcome\r home')  # \r	Carriage Return
print('Welcome \thome')  # \t	Tab

# BOOL
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

# OPERATORS
# arithmetic operator are as expected just like in any other language

# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y

# Assignment operators  are also as expected except the the ++ for incrementing one does not exist in python

# =	x = 5	x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# %=	x %= 3	x = x % 3
# //=	x //= 3	x = x // 3
# **=	x **= 3	x = x ** 3
# &=	x &= 3	x = x & 3
# |=	x |= 3	x = x | 3
# ^=	x ^= 3	x = x ^ 3
# >>=	x >>= 3	x = x >> 3
# <<=	x <<= 3	x = x << 3

#  Comparison operators

# ==	Equal	x == y
# !=	Not equal	x != y
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y

# Logical Operator

# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

# Identity operators

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# is 	Returns True if both variables are the same object	x is y
# is not	Returns True if both variables are not the same object	x is not y

# Membership Operators

# Membership operators are used to test if a sequence is presented in an object:
# in 	Returns True if a sequence with the specified value is present in the object	x in y
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

# LISTS
# List items are ordered, changeable, and allow duplicate values.
this_list = ['apple', 'banana', 'cherry', 'apple']
print(this_list)
print(len(this_list))

# the list constructor can be used to create a list
people = list(('Kevin', 'Justice', 'Aiden', 'Alex', 'Alodia'))
print(people)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and un-indexed. No duplicate members.
# Dictionary is a collection which is ordered* and changeable. No duplicate members.

# index accessment of list item
print(people[2:6])
print(people[-4:-1])

if 'Alodia' in people:
    print('Present Sir')

# CHANGE LIST
people[0] = 'Emma'
print(people)

people[1:3] = ['Richard', 'Lizzy']
print(people)

people[1:3] = ['Richard', 'Lizzy', 'Mike']
print(people)

people[1:3] = ['Nain']
print(people)

people.insert(2, 'Sandy')
print(people)

# ADD LIST ITEMS
#  use the append() method to append an element to a list .
people.append('Jacky')
print(people)
# to append a list to another list use the extend() method.

Members = ['Angel', 'Sarah', 'Nicole', 'Rhoda']
people.extend(Members)
print(people)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)

thistuple = ('machine', 'moto')
Members.extend(thistuple)
print(Members)

# REMOVE ITEMS

# The remove() method removes the specified item.
Members.remove('machine')
print(Members)

# The pop() method removes the specified index.

Members.pop(1)
print(Members)
Members.pop()  # removes the last item
print(Members)

# The del keyword also removes the specified index or the entire list:

del Members[2]
print(Members)

del Members
# print(Members)

# The clear() method empties the list.
# The list still remains, but it has no content.

# people.clear()
# print(people)

for x in people:
    print(x)
# print item by referring to their index
print()
for i in range(len(people)):
    print(people[i])
print()

# print from item index 2 to 4
for i in range(2, 5):
    print(people[i])

print()

users = list(('angel', 'sarah', 'nicole', 'rhoda'))


i = 0
while i < len(users):
    print(users[i])
    i += 1

    print()

# List comprehension offers the shortest syntax for looping through lists

[print(x) for x in people]  # shorthand for loop

print()

# normal looping through a list

fruits = ['mango', 'banana', 'cherry', 'apple', 'kiwi', 'orange']

newlist = ['watermelon']

for x in fruits:
    if 'a' in x:
        newlist.append(x)
        print(newlist)

print()

# comprehension of thesame loop
# The return value is a new list, leaving the old list unchanged.

# The condition is like a filter that only accepts the items that valuate to True.
newlist = [x for x in fruits if 'a' in x]
print(newlist)

print()

newUsers = [name for name in users if name != 'Rhoda']
print(newUsers)  # a new list without Rhoda

print()

newUsers = [name for name in users]
# a new list of thesame old data. prints out everything in the old list
print(newUsers)

print()

numbers = [x for x in range(10)]
print(numbers)  # result = an iteration of 0 - 9

print()

numbers = ['hey you' for x in range(10)]
print(numbers)  # hey you 10 times

print()

girls = [x.upper() for x in users if 'a' in x]
print(girls)  # a newlist of name with the alphabet a in it transformed to uppercase

print()

# return the item if is not nicole if it is nicole return KOSY
freshGirls = [x.upper() if x != 'nicole' else 'KOSY' for x in users]

print(freshGirls)

print()


# SORT LIST

fruits = ['mango', 'banana', 'cherry', 'apple', 'kiwi', 'orange', 'pineapple']
record = [100, 50, 65, 82, 23]

#  the sort method sorts the array in accending order.

fruits.sort()
print(fruits)
print()

record.sort()
print(record)
print()

# to reverse our sorted list we set reverse = true as an argument to the sort method

fruits.sort(reverse=True)
print(fruits)
print()

# we can also use the keyword (key=functionName) to set a function as our sort argument.


def myfunc(n):
    return abs(n - 90)


record.sort(key=myfunc)
print(record)
print()

# on default the sort method will sort uppercase before lowercase but we can overide this by using the str.lower as a key function.
fruitsUp = ['mango', 'banana', 'cherry',
            'apple', 'Kiwi', 'Orange', 'Pineapple']
fruitsUp.sort()
print(fruitsUp)
print()

fruitsUp.sort(key=str.lower)
print(fruitsUp)
print()

# we can reverse an unsorted list

fruitsUp.reverse()
print(fruitsUp)
print()

# COPY LIST
#  to copy a list we make use of the built in function copy() or list()

newGirls = users.copy()
print(newGirls)
print()

newFruits = list(fruits)
print(newFruits)
print()

# JOIN LIST
# to join a list we can use concatenation, append() or extend() methods

fruitGirls = fruits + girls
print(fruitGirls)
print()

for x in girls:
    fruits.append(x)
    print(fruits)
print()

girls.extend(newGirls)
print(girls)

# the count method checks how many of times an item appeared in a list while index show us the index of a particular item.
x = girls.count('sarah')
print(x)
print()

y = girls.index('rhoda')
print(y)
print()
