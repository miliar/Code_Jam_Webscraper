#!/usr/bin/env python
import sys
n = int(sys.stdin.readline())
for i in range(n):
    c,f,x = (float(j) for j in sys.stdin.readline()[:-1].split(' '))
    prev = float('+inf')
    j = 0
    while True:
        v = x/(2+f*j)+reduce(lambda y,z: y+c/(2+f*z),range(j),0)
        j+=1
        if v < prev:
            prev = v
        else:
            break
    print "Case #%d: %f" % (i+1, prev)
