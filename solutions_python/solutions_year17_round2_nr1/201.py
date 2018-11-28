import numpy as np
import scipy
import math


nt = int(raw_input())

for i_it in xrange(nt):
    d,n = map(int,raw_input().split())
    
    l = []
    for i in xrange(n):
        ki,si = map(int,raw_input().split())
        l.append((ki,si))
    
    for i in xrange(n-1,-1,-1):
        ti = (d - l[i][0])/float(l[i][1])
        if i+1 <= n-1:
            t = max(ti,t)
        else:
            t = ti
    
    va = float(d)/t
    
    print "Case #{}: {}".format(i_it+1,va)
    
