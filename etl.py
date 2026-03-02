
# notes: there is a slight buffer when you immediately run the python when changing the syntax, this is called output buffering.  this is due to performance reasons

import random

## comments

# this is a single-line comment

'''this is a multistring, 
but treated as a comment'''

## output statements

print('this is a print statement.')

print('''this is a  
      
print statement.''')

print('''this is a 
      print statement.''')

print('i am', 21, 'years old')

print('i can append to the last of the line by using end= ', end='')
print('then it would be treated as one line')

## variables

num1 = 5
num2 = num1 + 1

print(num1)
print(num2)

print(type(num1))
print(type(num2))

print('i can append like this', num2)

x = str(3)  #^ x will be '3'
y = int(3)  #^ y will be 3
z = float(3)  #^ z will be 3.0

# note that i reused the variables at the top, but python rewrites the old with the newest one
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

#^ fruits is a list, what i did is unpacking, extracting values into variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "osam"

def myfunc():
  print("Python is", x)

myfunc()

x = "bongbabe"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

x = 5
y = 'john'
print(type(y))

print(random.randrange(1,21))

x = "bang babe"
print(x[3])

bang = [1, 2]
for index in bang:
  print(index)

  a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("bang" in txt)

x = False

print(x + 1)

b = "Hello, World!"
print(b[-10:-2])

age = 36

txt = f"The price is {20 * 59} dollars"
print(txt)
