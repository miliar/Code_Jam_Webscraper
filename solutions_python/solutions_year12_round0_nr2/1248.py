#!/usr/bin/env python
import sys

n = int(raw_input())
for t in range(n):
    line = map(int, raw_input().split(' '))
    s = line[1]
    p = line[2]
    line = line[3:]
    res1 = sum([1 for i in line if i >= (max(0,p-1)+max(0,p-1)+p)])
    res2 = sum([1 for i in line if i >= (max(0,p-2)+max(0,p-2)+p) and i < (max(0,p-1)+max(0,p-1)+p)])
    print "Case #%d: %d" % (t+1, res1 + min(s, res2))

