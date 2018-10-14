#!/usr/bin/env python
from math import *
from sys import *

# N is a string
def findtidy(N):
    num = list(N)
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            for j in range(i,-1,-1):
                if (num[j] > num[j+1]):
                    num[j] = str(int(num[j])-1)
                    pivot = j
            return "".join(num[:pivot]) + str(int(num[pivot])) + "9"*(len(num) - pivot- 1)
    return N
        
numcases = int(stdin.readline())
for case in range(1,numcases+1):
    print "Case #" + str(case) + ": " + str(int(findtidy(stdin.readline().strip())))
