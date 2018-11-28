# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 21:40:04 2017

@author: sanindra
"""

for i in xrange(input()):
    d, n = map(int, raw_input().split())
    x    = 0.0
    for j in xrange(n):
        k, s = map(int, raw_input().split())
        x    = max(x, (d - k)/float(s))
    
    print "Case #{}: {}".format(i+1,"%.6f"% (d/x))
        
        