#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import math

trial = int(sys.stdin.readline())
for t in range(trial):
    [l,p,c] = [int(j) for j in sys.stdin.readline().split()]
    
    i=0
    while 1:
        if l*c**i>=p:
            if i-1==0:
                print "Case #%d: 0"%(t+1)
                break
            j=0
            while 1:
                if (2**j)>=i:
                    print "Case #%d: %d"%(t+1, j)
                    break
                else:
                    j+=1
            break
        else:
            i+=1
        
