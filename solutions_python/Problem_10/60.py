#!/usr/bin/env python

import sys
from copy import copy

f = open(sys.argv[1])
N = int(f.readline())

for caseno in range(1,N+1):
    P, K, L = map(int, f.readline().split())
    freqs = map(int, f.readline().split())

    freqs.sort()
    freqs.reverse()
    
    i = 1
    mul = 1
    count = 0
    for i in range(L):
        count = count + freqs[i] * mul 
        i = i + 1
        if i % K == 0:
            mul = mul + 1
            
        
    
    print "Case #%d: %d" % (caseno, count)
    

    
    
