#!/usr/bin/env python

#
# Copyright (c) 2012 J.M. Dana
#

import fileinput
import string
import sys
import os
import re
from copy import copy

def reachables(vines,current,prev):
    idx=current[2]
    
    for p,l,i in (vines[:idx] + vines[idx+1:])[::-1]:
        if p < current[0]:
            break
            
        if (p - current[0]) <= min(current[1],current[0] - prev[0]):        
            if l == -1:
                return True
            
            if reachables(vines,vines[i],current):
                return True
                                
    return False
    
    

def doit(vines):    
    if vines[0][1] < vines[0][0]:
        return 'NO'
        
    if vines[0][0] >= (vines[-1][0] - vines[0][0]):
        return 'YES'
    
    current = vines[0]
    prev = (0,0,0)
    
    return 'YES' if reachables(vines,current,prev) else 'NO'

theIN=fileinput.FileInput()

N = int(theIN.readline())

for case in range(1,N+1):
    Nvines=int(theIN.readline().strip('\n'))
    
    vines=[]
    
    for i in range(Nvines):
        vines.append(tuple(map(int,theIN.readline().strip('\n').split(' '))) + (i,))
    
    distance=int(theIN.readline().strip('\n'))
    vines.append((distance,-1,Nvines))
    
    print 'Case #%d: %s' % (case,doit(vines))

