#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,re

input = 'B-large.in.txt'
output = 'B-large.out.txt'
f = file(input)
g = file(output,'w')

n_cases = int(f.readline().strip())


def dot(x1,x2):
    temp = 0.0
    for i in range(3):
        temp += x1[i] * x2[i]
    return temp

def multiply(a, v):
    return [ a * x for x in v ]

def add(x1,x2):
    temp = []
    for i in range(3):
        temp.append(x1[i] + x2[i])
    return temp
    

for k in range(n_cases):
    
    N = int(f.readline().strip())
    fireflies = []
    
    r = [0,0,0]
    v = [0,0,0]
    for i in range(N):
        (x,y,z,vx,vy,vz) = f.readline().strip().split()
        r[0] += int(x)
        r[1] += int(y)
        r[2] += int(z)
        v[0] += int(vx)
        v[1] += int(vy)
        v[2] += int(vz)
    r = [x * 1.0 / N for x in r]
    v = [x * 1.0 / N for x in v]
    #print r,v
    
    if dot(v,v) > 0:
        t_min = - dot(r,v) / dot(v,v)
    if dot(v,v) == 0 or t_min < 0:
        t_min = 0.0
    r_min = add(r, multiply(t_min,v))
    d_min = dot(r_min,r_min) ** .5
    
    #print d_min,t_min
    
    line = "Case #%d: %.8f %.8f" % (k+1, d_min, t_min)
    print line
    g.write("%s\n" % line)

f.close()
g.close()
