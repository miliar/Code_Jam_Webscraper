#!/usr/bin/env python

#
# Copyright (c) 2012 J.M. Dana
#

import fileinput
import string
import sys
import os
import re

def doit(S,P,results):
    n=0
    
    for r in results:
        if r<P:
            continue
            
        if P*3 <= (r+2):
            n+=1
        elif (P*3 <= (r+4)) and S>0:
            n+=1
            S-=1
                        
    return n

theIN=fileinput.FileInput()

N = int(theIN.readline())

for case in range(1,N+1):
    line=map(int,theIN.readline().strip('\n').split(' '))
    num,S,P=line[0:3]
    results=line[3:]

    print 'Case #%d: %s' % (case,doit(S,P,results))

