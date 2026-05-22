# Python map() function
#map()function,it is a higher-order function used for uniform element-wise transformations,
#enabling concise and efficient code.A simple example of using map() to convert a list of
#strings into a list of integers.
s = ['1', '2', '3', '4']
res = map(int, s) # changes their datatypes from string to int
print(list(res))

#Converting map object to a list
#By default,map()fxn returns a map object,which is an iterator.
#Example;let's see how to double each elements of the given list.
# Custom function to be applied in map
def double(val):
    return val * 2
# Let us apply double on every member
a = [1, 2, 3, 4]
res = list(map(double, a)) # applies double to each element in a
print(res)

# map() with lambda; to make code shorter and easier
# let's see how to improve above code for better readability
a = [1, 2, 3, 4]
res = list(map(lambda x: x ** 2, a)) # squares each number and convert into a list
print(res)

# map() with multiple iterables;If the function we are applying takes morethan one argument
#Example;map() takes two iterables (a and b) and applies lambda fxn to add corresponding 
a = [1, 2, 3]
b = [4, 5, 6] #map() takes x from a and y from b and adds them
res = map(lambda x, y: x + y, a, b)
print(list(res))

# Converting string to Uppercase
#The example below shows how we can use map() to convert a list of strings to uppercase
fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)
print(list(res))

# Extracting first character from strings
# we use map() to extract the first character from each string in a list
words = ['apple', 'banana', 'cherry']
res = map(lambda s: s[0], words)  # Extract first character from each string inthe list
print(list(res))

# removing whitespaces from strings
# using map() to remove leading and trailing whitespaces from each string in a list
s = ['  hello  ', '  world  ', '  python  ']
res = map(str.strip, s)  #removes leading and trailing whitespaces from each string in list
print(list(res)) 

# Calculate fahrenheit from celsius 
# the example below use map() to convert a list of temperatures from celsius to Fahrenheit
celsius = [0, 20, 37, 100]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius) #Converts each celsius temp to Fahren..
print(list(fahrenheit))


# reduce()in Python (from functools)
#It applies a function cumulatively to an iterable,reducing it to a single value
#note; avoid it for complex logicor when intermediate results are needed
from functools import reduce
li = ["Geeks", "for", "Geeks"]
res = reduce(lambda x, y: x + " " + y, li) #Takes two strings at a time and concatenates
print(res) # them with a space 

#Example 1- Basic Usage with a Named Function
#This code uses reduce()fxn to accumulate values in alist by repeatedly addx two nums at a time
from functools import reduce
def add(x, y):
    return x + y #Defines a fxn that returns sum of two numbers
a = [1, 2, 3, 4, 5]
res = reduce(add, a) # applies add cumulatively to the list
print(res)

#Example 2- Using reduce() with a Lambda Function
#This example shows how lambda func can be used with reduce()to calculate factorial of a
# number by multiplying all elements of a list
from functools import reduce
a = [1, 2, 3, 4, 5]
res = reduce(lambda x, y: x * y, a) # multiplies elements step by step
print(res)

#Example 3- Using reduce() with Operator Module
#This exaple uses 'functool.reduce()' with built-in func from 'operator module' to perform
# Sum, product and string concatenation on lists
import functools
import operator
a = [1, 3, 5, 6, 2]
print(functools.reduce(operator.add, a))  # adds all numbers in the list
print(functools.reduce(operator.mul, a))  # multiplies all numbers in the list
print(functools.reduce(operator.add, ["geeks", "for", "geeks"])) #Concatenates all strings inlist

#Example 4- using initializer
#This code uses reduce()with a lambda func and an initial value to sum a list,starting
from functools import reduce  #from a given number
a = [1, 2, 3]
res = reduce(lambda x, y: x + y, a, 10) #starts with 10 as initial value, then adds 
print(res) # each elements in the list

# Differences Between reduce() and accumulate()
#accumulate() returns an iterator of intermediate results,while reduce()returns only final values
#This code shows how accumulate() from itertools module works,it  performs cumulative
from itertools import accumulate  #operation and return all intermediate results instead
from operator import add  # of just a single final value
a = [1, 2, 3, 4, 5]
res = accumulate(a, add) # adds elements cumulatively
print(list(res))

















