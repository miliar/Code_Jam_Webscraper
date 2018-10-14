#!/usr/bin/python

# google code jam - c.durr - 2012

# Dancing With the Googlers
# glouton


from string import *

def readint():    return int(raw_input())
def readarray(f): return map(f, raw_input().split())

def canReachMax(ti, p, diff):
    q = max(0, p-diff)
    return ti>=p+2*q

for test in range(readint()):
    tab = readarray(int)
    N = tab[0]
    S = tab[1]
    p = tab[2]
    t = tab[3:]
    res = 0
    for ti in t:
        if canReachMax(ti, p, 1): # not surprising
            res += 1
        elif canReachMax(ti,p,2) and S>0: # suprising
            res += 1
            S   -= 1
    print "Case #%i:"% (test+1), res
    
    
    
