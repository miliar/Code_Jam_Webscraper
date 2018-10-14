#!/bin/python
import sys

a = [[x for x in x.split()] for x in sys.stdin.readlines()]
b = a.pop(0)
c = [x[1] for x in a]
d = [[int(x) for x in str(x)] for x in c]

for w,x in enumerate(d):
    l=0;
    m=[]
    for i,j in enumerate(x):
        m.append(i-l)
        l+=j
    print('Case #%d: %d'%(w+1,max(m)))
