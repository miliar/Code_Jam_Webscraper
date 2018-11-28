# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 18:36:16 2017

@author: Giovanni
"""
import sys

inp = open(sys.argv[1],'r')
t = int(inp.readline())

for c in range(t):
    
    maxtime = 0
    d, h = [int(k) for k in inp.readline().split(" ")]
    
    for i in range(h):
        pos, speed = [int(k) for k in inp.readline().split(" ")]
        
        time = (d - pos)/float(speed)
        
        if time > maxtime:
            maxtime = time
    aspeed = d/maxtime
    
    
    print("Case #{}: {}".format(c+1, "%.6f" % aspeed))