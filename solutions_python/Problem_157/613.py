# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:22:52 2015

@author: petrs
"""

from math import ceil

f = open('C:\Users\petrs\Downloads\C-small-attempt0.in', 'r')
g = open('C:\Users\petrs\Downloads\soutput3.txt', 'w')

def q_mult(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return w, x, y, z

d = dict()
d["i"] = (0,1,0,0)
d["j"] = (0,0,1,0)
d["k"] = (0,0,0,1)

T = int(f.readline().split()[0])

for i in range(T):
    X,L = [int(x) for x in f.readline().split()]
    Pi = f.readline().split()[0]
    T = Pi * L

    val = (1,0,0,0)
    for t in T:
        val = q_mult(val, d[t])
    
    if val == (-1,0,0,0):
        valL = (1,0,0,0)
        for j in range(len(T)):
            valL = q_mult(valL, d[T[j]])
            if valL == d["i"]: break
        valP = (1,0,0,0)
        for k in range(len(T))[::-1]:
            valP = q_mult(d[T[k]], valP)
            if valP == d["k"]: break
        if valL == d["i"] and valP == d["k"] and j<k:
            g.write("Case #%i: YES\n" % (i+1))
        else:
            g.write("Case #%i: NO\n" % (i+1))
    else:    
        g.write("Case #%i: NO\n" % (i+1))


f.close()
g.close()