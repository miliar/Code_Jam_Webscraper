#!/usr/bin/env python

import sys
import re

lines = sys.stdin.readlines()
lines = lines[1:]
i = 0
for line in lines:
    i += 1
    ary = map(lambda x:int(x), line.split(" "))
    (l,t,n,c) = ary[0:4]
    a = ary[4:]
    stars = (a * ((n / len(a)) +1))[0:n]
    
    time = 0
    while True:
        if len(stars) == 0: break

        if stars[0]*2 < t:
            time += stars[0]*2
            t -= stars[0]*2
            stars = stars[1:]
        else:
            stars[0] -= t*0.5
            time += t
            break

    stars.sort(reverse=True)
    time += reduce(lambda x,y: x+y, stars[0:l],0)
    time += reduce(lambda x,y: x+y, map(lambda x:x*2, stars[l:]),0)

    print >>sys.stdout, "Case #%d: %d" %  (i, time)

    
