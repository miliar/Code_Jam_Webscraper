#!/usr/bin/python

# google code jam - c.durr - 2011

# Problem B. Spinning Blade

try:
    import psyco
except:
    pass

from math      import *

def readint():    return int(raw_input())
def readarray(f): return map(f, raw_input().split())

def solve():
    for K in range(min(R,C),2,-1):
        for r in range(R-K+1):
            for c in range(C-K+1):
                ar = 0
                ac = 0
                for i in range(K):
                    for j in range(K):
                      if not (i in [0,K-1] and j in [0,K-1]):
                          ar += (2*i-K+1) * W[r+i][c+j]
                          ac += (2*j-K+1) * W[r+i][c+j]
                if ar==0 and ac==0:
                    return K
    return "IMPOSSIBLE"

for test in range(readint()):
    R,C,D = readarray(int)
    W = []
    for r in range(R):
        W.append(map(int,raw_input()))
        
    print "Case #%i:"% (test+1), solve()
    
    
    
