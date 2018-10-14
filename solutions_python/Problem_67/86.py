#!/usr/bin/python

# google code jam - c.durr - 2010

#
#

try:
    import psyco
except:
    pass


from math import *

def readint():    return int(raw_input())
def readarray(f): return map(f, raw_input().split())

def simulate(d):
    for x in range(100,0,-1):
        for y in range(100,0,-1):
            n = d[x-1][y] + d[x][y-1]
            if (n==0):
                d[x][y] = 0
            elif (n==2):
                d[x][y] = 1

def empty(d):
    return  sum(map(sum,d))==0

def printB(d):
    for i in range(8):
        for j in range(8):
            print d[i][j],
        print
    print

for test in range(readint()):
    R = readint()
    d = [[0 for _ in range(101)] for _2 in range(101)]
    for r in range(R):
        x1,y1,x2,y2 = readarray(int)
        for x in range(x1, x2+1):
            for y in range(y1,y2+1):
                d[x][y] = 1
    time = 0
    while (not empty(d)):
        simulate(d)
        time += 1

    print "Case #%i:"% (test+1), time
    
    
