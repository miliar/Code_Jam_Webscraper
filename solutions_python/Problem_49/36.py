# -*- coding: utf-8 -*-
import math

fin = open("d.in","r")
T = int(fin.readline())

def d(a, b):
    dist = math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    if abs(a[2]-b[2]) > dist:
        return max(a[2], b[2])
    return (a[2] + b[2] + dist) / 2.0
    
    
for i in range(1,T+1):
    n = int(fin.readline())
    
    p = []
    for j in range(n):
        x, y, r = map(int, fin.readline().split())
        p.append((x,y,r))
    
    R = 0;
    if n == 1:
        R = p[0][2]
    elif n == 2:
        R = max(p[0][2], p[1][2])
    elif n == 3:
        R1 = max(d(p[0], p[1]), p[2][2])
        R2 = max(d(p[1], p[2]), p[0][2])
        R3 = max(d(p[2], p[0]), p[1][2])
        R = min(R1, R2, R3)
    else:
        exit(1)
    
    print "Case #%d: %.6f" % (i, R)
        