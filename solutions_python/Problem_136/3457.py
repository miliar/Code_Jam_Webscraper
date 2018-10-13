#!/usr/bin/env python
import sys

f=open('B-small-attempt0.in')
fo=open('B-small.out','w')
cases = f.readline().rstrip()
for a in range(1,int(cases)+1):
    fo.write("Case #%d: " % a)
    (fcost, fprod, goal) = f.readline().rstrip().split()
    fcost = float(fcost)
    fprod = float(fprod)
    goal = float(goal)
    previous = (goal / 2.0) + 1
    current = 0.0
    farms = 0
    while previous > current:
        if (current > 0.0):
            previous = current
        current = 0.0
        for i in range(farms):
            current += fcost/(2.0 + fprod*i)
        current += goal/(2.0 + fprod*farms)
        farms += 1
    fo.write('%.7f\n' % previous)
fo.close()
f.close()
    
