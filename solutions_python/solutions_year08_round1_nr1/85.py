#!/usr/bin/python

# Run by:
#     cat input | a.py

import sys
from math import sqrt

l = sys.stdin.readline()
n = int(l)

for i in range(n):
    print 'Case #%d:' % (i+1,),

    l = sys.stdin.readline()
    n_degrees = int(l)

    l = sys.stdin.readline()
    v1 = [int(x) for x in l.split()]
    l = sys.stdin.readline()
    v2 = [int(x) for x in l.split()]
    
    assert len(v1) == n_degrees
    assert len(v2) == n_degrees
    
    v1.sort()
    v2.sort()
    v2.reverse()
    
    product = 0L
    for i in range(n_degrees):
        product += v1[i]*v2[i]
    
    print product
    
