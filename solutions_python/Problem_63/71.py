#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Graham Dennis on 2010-05-23.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
from math import log, ceil, fabs

bc = [None] * 40

eps = 1e-10

def binomialCost(divisions):
    if divisions == 1: return 0
    if bc[divisions] is None:
        bc[divisions] = 1 + binomialCost((divisions+1)//2)
        
    return bc[divisions]

def main():
    f = file(sys.argv[1])
    
    T = int(f.readline())
    for t in xrange(T):
        L, P, C = map(int, f.readline().split())
        
        diff = log(float(P)/float(L))
        
        divisions = int(ceil((diff)/log(C) - eps))
        result = binomialCost(divisions)
        
        print "Case #%i: %i" % (t+1, result)
    

if __name__ == '__main__':
    main()

