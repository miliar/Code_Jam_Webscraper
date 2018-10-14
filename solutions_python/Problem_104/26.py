#!/usr/bin/python

# google code jam - c.durr - 2012

#
#

try:
    import psyco
except:
    pass

from math import *
from fractions import *

def readint():    return int(raw_input())
def readarray(f): return map(f, raw_input().split())

def solve(S):
    global C
    C = [' ' for _ in range(len(S))]
    if backtrack(len(S)-1, 0, sum(S)):
        for c in ['A','B']:
            for i in range(len(C)):
                if c==C[i]:
                    print S[i],
            print
    else:
        print "Impossible"

def backtrack(i,A_B, rem):
    if i==-1:
        return A_B==0 and rem!=sum(S)
    if A_B==rem:
        for j in range(i):
            C[j]='B'
        return True
    if A_B==-rem:
        for j in range(i):
            C[j]='A'
        return True
    if abs(A_B)>rem:
        return False
    C[i] = ' '
    if backtrack(i-1, A_B, rem):
        return True
    x = S[i]
    C[i] = 'A'
    if backtrack(i-1, A_B+x, rem-x):
        return True
    C[i] = 'B'
    if backtrack(i-1, A_B-x, rem-x):
        return True
    return False

for test in range(readint()):
    t = readarray(int)
    N = t[0]
    S = t[1:]
    print "Case #%i:"% (test+1)
    solve(S)
    
    
