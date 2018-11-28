#!/usr/bin/env python

import sys
import re

lines = sys.stdin.readlines()
lines = lines[1:]
i = 0
for line in lines:
    i += 1
    rb = {'O':[1,0], 'B':[1,0]} # (pos, time)
    time = 0
    for m in re.finditer(r"(O|B) +(\d+)", line):
        (r, p) = m.groups()

        if r == 'O':
            o = 'B'
        else:
            o = 'O'

        pos = int(p)
        if rb[r][1] < abs(pos - rb[r][0]):
            spent = abs(pos - rb[r][0]) - rb[r][1] + 1
        else:
            spent = 1

        time += spent

        rb[r] = [pos,0]
        rb[o][1] += spent
    print >>sys.stdout, "Case #%d: %d" %  (i, time)


