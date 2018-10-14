# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:25:24 2017

@author: lucas
"""

import sys

def removeFirst(p):
    x = 0
    while(x < len(p) and pan[x] == '+'):
        x += 1
    return p[x:]
def flipC(c):
    return '+' if c == '-' else '-'
def flip(p, k):
    return [p[i] if i >= k else flipC(p[i]) for i in range(len(p))]

infile = sys.stdin

lines =  [l.replace('\n','').split(' ') for l in infile][1:]
cases =  [[list(x[0]),int(x[1])] for x in lines]

caseID = 1
for c in cases:
    size = c[1]
    pan = c[0]
    ops = 0
    while(len(pan) != 0 and len(pan) >= size):
        pan = removeFirst(pan)
        if(len(pan) >= size):
            ops += 1
            pan = flip(pan, size)
            #print(pan)
    print('Case #{}: '.format(caseID), end='')
    if(len(pan) == 0):
        print(ops)
    else:
        print('IMPOSSIBLE')
    caseID += 1