#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import math

#f=open("A-small-attempt0.in")
#f=open("A-large.in")
#w=open("out.txt", "w")
#t = int(f.readline())
t = int(sys.stdin.readline())
for i in range(t):
    [n,k] = [int(j) for j in sys.stdin.readline().split(' ')]
    ###[n,k] = [int(j) for j in f.readline().split(' ')]
    if n==0: onoff="ON"
    elif k==0: onoff="OFF"
    else:
        p = int(math.pow(2, n))
        if k%p==(p-1): onoff="ON"
        else: onoff="OFF"
    print "Case #%d: %s"%(i+1,onoff)
    ###w.write("Case #%d: %s\n"%(i+1,onoff))
    
