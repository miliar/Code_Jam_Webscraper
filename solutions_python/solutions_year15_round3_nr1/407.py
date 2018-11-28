#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# google code jam - c.durr - 2015 - 1B

# Brattleship
# complexity O(1)

from math      import *
from fractions import *
from sys       import *

def readstr():    return stdin.readline().strip()
def readint():    return int(stdin.readline())
def readarray(f): return list(map(f, stdin.readline().split()))

def solve(R,C,W):
    if W==1:
        return R*C
    else:
        return R*((C-1)//W) + W

for test in range(readint()):
    R,C,W = readarray(int)
    print("Case #%i: %i"% (test+1, solve(R,C,W)))
    
    
