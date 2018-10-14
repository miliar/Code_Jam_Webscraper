#!/usr/bin/env python

import sys
import re

lines = sys.stdin.readlines()
lines = lines[1:]
i = 0
while i*2 < len(lines):
    (l1,l2) = lines[i*2:i*2+2]
    (n,l,h) = map(lambda x:int(x), l1.split(" "))
    freqs = map(lambda x:int(x), l2.split(" "))
    i+=1
    for j in range(l,h+1):
        for f in freqs:
            if (j % f != 0) and (f % j != 0): break
        else:
            print >>sys.stdout, "Case #%d: %d" %  (i,j)
            break
    else:
        print >>sys.stdout, "Case #%d: NO" %  i
