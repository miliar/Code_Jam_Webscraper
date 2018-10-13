'''
Created on Apr 13, 2013

@author: ericdennison
'''
# how many fair (palindromic) and square (squar root is palindromic)

"""
3
1 4
10 120
100 1000

Case #1: 2
Case #2: 0
Case #3: 2

mine:
Case #1: 2
Case #2: 0
Case #3: 2

"""

import math
from decimal import Decimal, getcontext

getcontext().prec = 110

def fair(n):
    s = str(n)
    return s == s[::-1]

def fairandsquare(n):
    #print n
    s = n.sqrt()
    return s._isinteger() and fair(n) and fair(s)

def drange(a,b):
    r  = []
    if a >= b:
        return r
    x = a
    while x < b:
        r.append(x)
        x += 1
    return r

f = file("C-small-attempt0.in").readlines()
fo = file("outputC.txt",'w')
ncases = int(f[0])

for i in range(0,ncases):
    a,b = [Decimal(s) for s in f[i+1].split()]
    fo.write( "Case #{0}: {1}\n".format(i+1,[fairandsquare(n) for n in drange(a,b+1)].count(True)))
        
