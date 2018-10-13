#!/usr/bin/env python

import sys
import re

lines = sys.stdin.readlines()
lines = lines[1:]
i = 0
for line in lines[1::2]:
    i += 1
    a = map(int, line.split(" "))

    if 0 != reduce(lambda x,y: x^y, a):
        print >>sys.stdout, "Case #%d: NO" % i
        continue

    a.sort()
    print >>sys.stdout, "Case #%d: %d" % (i, reduce(lambda x,y:x+y, a[1:]))
