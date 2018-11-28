#!/usr/bin/python
import sys
import math
inp = sys.stdin.readlines()
num_cases = int(inp[0])
cases = [(int(r), int(t)) for r, t in [l.split() for l in inp[1:]]]

for num, case in enumerate(cases):
    rings = 0
    radius = case[0]
    remaining_paint = case[1]
    
    radius += 1
    
    while remaining_paint >= radius**2 - (radius-1)**2:
        rings += 1
        remaining_paint -= radius**2 - (radius-1)**2
        radius += 2
    
    print "Case #%d: %d" % (num+1, rings)