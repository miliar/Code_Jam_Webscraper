#!/usr/bin/python

# google code jam - c.durr - 2010

# Fair Warning

# compute the gcd of all numbers |ti-tj| (over all i<j)
# let T be this number.
# then compute smallest y s.t. (t1+y) is multiple of T

import sys

def gcd(a,b):
    '''Euclid's algorithm'''
    if (b==0):
        return a
    return gcd(b, a-b*(a/b))

def gcdSet(S):
    a = 0
    for b in S:
        a = gcd(b,a)
    return a


C = int(raw_input())
for c in range(C):
    L = map(int, raw_input().split()) 
    N = L[0]
    t = L[1:]  

    S = [abs(t[i]-t[j]) for j in range(N) for i in range(j)]
    T = gcdSet(S)
    
    y = (T-t[0]%T)%T
    print "Case #%i:"%(c+1), y
    
