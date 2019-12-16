#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:23:46 2019

@author: akemberling
"""

# Working Through Data Carpentry Lessons for Ecologists
# Source: https://datacarpentry.org/python-ecology-lesson/01-short-introduction-to-Python/index.html


#Operators
3 + 12 #Addition
2 * 2  #Multiplication
2 **4  #Power
13 % 5 #Modulo

#Logical Operators
3 > 4 #False
3 < 4 #TRUE

#Sequences Lists and Tuples


#Lists
numbers = [1, 2, 3]
numbers[0]
type(numbers)


#for Loop
for num in numbers:
    print(num)

#Adding elements to a list using append method
numbers.append(4)
print(numbers)

#Methods are ways to interact with an object
# numbers. + tab will display available methods
numbers.count(2)

#help will display what the methods do and how to use them
help(numbers)

#Tuples, cannot be changed
a_tuple = (1, 2, 3)
another_tuple = ('blue', 'green', 'red')

# Note: lists use square brackets
a_list = [1, 2, 3]

a_list[1] = 5 #Lists can be changed
a_tuple[2] = 5 #tuples can not


#Dictionaries are containers that hold pairs of objects, like a named list
translation = {'one': 1,'two':2}
translation['one']

#To add to a dictionary we assign a new value to a new key
rev = {1: 'one', 2: 'two'}
rev[3] = 'three'
rev


#For loops with dictionaries
for key, value in rev.items():
    print(key, '->', value)

#or
    
for key in rev.keys():
    print(key, '->', rev[key])
    
# Functions
def add_function(a, b):
    result = a + b
    return result

z = add_function(20, 22)
print(z)





