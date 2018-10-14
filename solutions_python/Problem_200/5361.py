# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:57:49 2017

@author: JPGallagher
"""
def is_tidy(number):
    str_number = str(number)
    for digit in range(1,len(str_number)):
        if int(str_number[digit-1]) > int(str_number[digit]):
            return False
    return True

def largest_tidy_n(n:int):
    testing_tidy_num = n
    while is_tidy(testing_tidy_num) == False:
        testing_tidy_num -=1
    return testing_tidy_num

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
n = ['']*t
for i in range(0, t):
    n[i] = int(input())  # read a list of integers, 2 in this case
for i in range(1,len(n)+1): 
    print("Case #{}: {}".format(i, largest_tidy_n(n[i-1])))
  # check out .format's specification for more formatting opt