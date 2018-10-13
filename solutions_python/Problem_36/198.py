#! /usr/bin/env python

import sys
import re
f = open(sys.argv[1])
N = int(f.readline().strip())
w = "welcome to code jam"[::-1]
for i in xrange(N):
    s = f.readline().strip()
    s = s[::-1]
    p = [0]*19;
    for c in s:
        for wc,l in enumerate(w):
            if c == l:
                if wc == 0:
                    p[wc] += 1
                else:
                    p[wc] += p[wc-1]
    print "Case #%d: %04d"%(i+1,p[-1])
