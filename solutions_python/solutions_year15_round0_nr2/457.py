#!/usr/bin/env python3

import sys, math

def computeTime (x, P):
    acum = 0
    for p in P:
        if p > x:
            if p % x == 0:
                acum = acum + int(p/x) - 1
            else:
                acum = acum + int(math.floor(p/x))
    return acum + x

def linearSearch (P):
    prevt = float('inf')
    prevs = float('inf')
    for size in range(1, max(P)+1):
        t = computeTime (size, P)
        #print (t, prevt)
        if t < prevt:
            prevt = t
            prevs = size
    #print (prevs, prevt)
    return prevt

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for t in range(1, T+1):
        D = int(sys.stdin.readline())
        P = [int(x) for x in sys.stdin.readline().split()]
        print ("Case #%d: %d" % (t, linearSearch(P)))
        
