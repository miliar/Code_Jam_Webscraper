#!/usr/bin/python
from __future__ import generators
import sys

def ReadInts():
    return map(int, sys.stdin.readline().strip().split())

def run(a):
    t=0
    vx_all,vy_all,vz_all = 0.0,0.0,0.0
    x_all,y_all,z_all = 0.0,0.0,0.0
    for line in a:
        x,y,z,vx,vy,vz=line
        x_all += x
        y_all += y
        z_all += z
        vx_all += vx
        vy_all += vy
        vz_all += vz
    n=len(a)
    a,b,c=x_all/n,y_all/n,z_all/n
    x,y,z=vx_all/n,vy_all/n,vz_all/n
    if x==0 and y==0 and z==0:
        return t,(a**2+b**2+c**2)**0.5
    t= -(a*x+b*y+c*z) / (x**2+y**2+z**2)
    if t<0:
        t=0
    return t,((x*t+a)**2+(y*t+b)**2+(z*t+c)**2)**0.5

num_cases = ReadInts()[0]
for i in xrange(1, 1+num_cases):
    num_vectors = ReadInts()[0]
    a=[]
    for _ in xrange(num_vectors):
        a.append(ReadInts())
    result = run(a)
    print "Case #%d: %.8f %.8f" % (i, result[1], result[0])
