#!/usr/bin/env python

import sys

nc = 1

ls = sys.stdin.readlines()
t = int(ls[0])
ls = ls[1:]
for l in ls:
    _, b = l.split()
    need = 0
    sum = 0
    for i, x in enumerate(b):
        need = max(need, i - sum)
        sum += int(x)
    print "Case #%d: %d" % (nc, need)
    nc += 1
    
