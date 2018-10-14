# Python version 2.7
import sys
import math

def checkOne(x):
    s = str(x)
    for j in range(len(s)/2):
        if s[j] != s[-j-1]: return False
    y = x**2
    s = str(y)
    for j in range(len(s)/2):
        if s[j] != s[-j-1]: return False
    return True

def oneCase():
    [a,b] = map(int, sys.stdin.readline().split(' '))
    count = 0
    for i in range(int(math.sqrt(a)),int(math.sqrt(b))+1):
        if checkOne(i):
            j = i**2
            if a <= j and j <= b: count += 1
    return str(count)
    

cases = int(sys.stdin.readline())
for i in range(cases):
    print "Case #" + str(i+1) + ": " + oneCase() 