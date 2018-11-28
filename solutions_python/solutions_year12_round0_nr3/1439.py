#!/usr/bin/env python

import sys

f = open(sys.argv[1])
t = int(f.readline())


def r(x,y):
    sx = str(x)
    sy = str(y)
    s2 =''
    for i in range(1,len(sx)):
        s2 = sx[-(i):] + sx[0:len(sx)-(i)]
        if (s2==sy):
            return True
    return False

for i in range(t):
    a,b = map( int , f.readline().split())

    count=0
    for n in range(a,b+1):
        for m in range(n+1,b+1):
            if r(n,m):
                count+=1
    print "Case #%d: %d" %((i+1),count)
