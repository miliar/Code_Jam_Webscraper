# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:29:57 2015

@author: vbd
"""

inp = raw_input()
T = int(inp)

for c in range(1,T+1) :
    inp = raw_input()
    S = inp.split(' ')
    Smax = int(S[0])
    
    y = 0
    p = 0
    
    for i in enumerate(S[1]):
        if i[0] > Smax:
            break
        if (i[0] > (p + y)):
            y = i[0] - p
        p += int(i[1])
    print "Case #{0}: {1}".format(c,y)