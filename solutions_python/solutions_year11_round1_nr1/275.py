#!/usr/bin/env python

import sys
import re

def is_int(a):
    return (a - int(a)) < 1e-14

lines = sys.stdin.readlines()
lines = lines[1:]
i = 0
for line in lines:
    i += 1
    possible = False
    (n, pd, pg) = map(lambda x: int(x),line.split(" "))

    for j in range(1,n+1):
        if is_int(j * (pd / 100.0)):
            if (0 < pd and pg == 0) or (pd < 100 and pg == 100):
               continue
            possible = True
            break

    print >>sys.stdout, "Case #%d: %s" %  (i, (possible and "Possible") or "Broken")
