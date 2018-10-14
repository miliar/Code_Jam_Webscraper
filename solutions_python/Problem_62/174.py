#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
import sys
rdl = lambda: sys.stdin.readline().replace("\n", '')
sys.setrecursionlimit(5000)

 
def solve(wires):
    if len(wires) == 1:
        return 0
    
    a, b = wires[0]
    
    total = 0
    for q, w in wires[1:]:
        if (a>q) != (b>w):
            total += 1
    return total + solve(wires[1:])
 
def process(case):
    N = int(rdl())
    
    wires = []
    for dumb in xrange(N):
        a, b = [int(i) for i in rdl().split()]
        wires.append((a, b))
    
    return solve(wires)
 
cases = int(rdl())
for case in xrange(1, cases+1):
    print "Case #%d:"%case, process(case)