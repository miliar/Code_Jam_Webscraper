#!/usr/bin/python

import os
import sys
import math

def log2(int1=1):
    return(int(math.log(int1)/math.log(2)+.00001))

fn = sys.argv[1]

fh = open(fn, "r")
lines = fh.readlines()
T = int(lines[0].strip())
cases = map(lambda x: map(int,x.strip().split(" ")), lines[1:])
fh.close()
#print cases


fh = open("b.out","w")
for (i,case) in enumerate(cases):
    C = case[2]
    min1 = case[0]*C
    max1 = case[1]
    atests = 0 
    while min1 < max1:
        atests +=1
        min1 = min1 * C
    if atests == 0:
        print >> fh, "Case #"+str(i+1)+": 0" 
    if atests == 1:
        print >> fh, "Case #"+str(i+1)+": 1" 
    if atests >1:
        print >> fh, "Case #"+str(i+1)+": "+str(log2(atests)+1) 
