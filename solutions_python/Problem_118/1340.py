import itertools
import numpy


with open('/home/vivanov/Downloads/C-small-attempt0.in') as f:
    lines = f.read().splitlines()[1:]
    l = []
    for i in lines:
        l.append([ int(k) for k in i.split(' ')])
    print l


def is_palindrome(x):
    s = list(str(x))
    if len(s) % 2 == 1:
        del s[len(s)/2]
    return s[:len(s)/2] == list(reversed(s[len(s)/2:]))

import math


def is_square (x):
    if math.modf(x ** 0.5)[0] == 0:
        return is_palindrome(int(x ** 0.5))
    
print is_palindrome (11211)
print is_square(9)

def check_interval(a,b):
    counter = 0
    for x in range(a,b+1):
        if is_palindrome(x) and is_square(x):
            counter += 1
    return counter
        

with open('fair_and_square.out', 'w') as f :
    to_write = []
    for i in range(len(l)):
        to_write.append(('Case #%s: ' %(i+1)) + str(check_interval(l[i][0], l[i][1])) + '\n')
    f.writelines(to_write)

    
    
