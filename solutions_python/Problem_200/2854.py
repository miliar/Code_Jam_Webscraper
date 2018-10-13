# python ProblemB.py < inputSmall.txt > outputSmall.txt

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:52:07 2017

@author: maxime dimidschstein
"""
import math

def inOrder(n):
    while n>=10:
        if n%10 < (n//10)%10:
            return False
        n = int(n//10)
    return True
    
def toRemove(n, l):
    i = n//math.pow(10,(l-1))
    for k in range(2, l+1):
        j = n//math.pow(10,(l-k))
        if (i%10)>(j%10):
            return int(n-i*math.pow(10,(l-k+1))+1)
        i=j
    return 0

def order(n, l):
    res = n-toRemove(n, l)
    if(not inOrder(res)):
        return order(res, l)
    return res

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for m in range(1, t + 1):
    s = input()
    l = len(s)
    n = int(s)
    res = ""
    if l==1:
        res=n
    else:
        res = int(order(n, l))
    print("Case #{}: {}".format(m, res))