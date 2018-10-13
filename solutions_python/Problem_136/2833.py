#!/usr/bin/python
# cookieclicker.py - Sumit Mahamuni


import sys
sys.setrecursionlimit(10000)
filename = sys.argv[1]

def winning_time(c, f, x, p = 2):
    if (x/p) > ((c/p) + x / (p + f)):
        time = c/p + winning_time(c,f,x, p + f)
    else:
        time = x / p
    return time
    

with open(filename) as file:
    numberOfTestCases = int(file.readline())
    for example in range(1,numberOfTestCases+1):
        C, F, X = file.readline().strip().split(' ')
        print "Case #"+str(example)+": "+str(round(winning_time(float(C),float(F),float(X)),7))

