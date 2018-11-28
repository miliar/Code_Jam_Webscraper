#!/usr/bin/python

from sol import *

c = next_int()

for x in range(1,c+1):

    K = next_int()
    n = next_int()

    d = [ next_int()-1 for i in range(n) ]
    
    tab = range(K)
    out = range(K)

    idx = 0
    for i in range(1,K+1):
        idx = (idx + i-1) % len(tab)
        out[ tab[idx] ] = i

        tab.remove( tab[idx] )

    print 'Case #%d: ' % x,
    for dd in d:
        print out[dd],
    print 
