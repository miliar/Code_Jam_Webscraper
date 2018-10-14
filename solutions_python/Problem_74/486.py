#!/usr/bin/env python

import os
import sys

t = int(sys.stdin.readline())

for test in range(t):
    line = sys.stdin.readline().split()
    n = int(line[0])
    red = [1,0]
    blue = [1,0]
    ret = 0
    for i in range(n):

        pos = int(line[2*i+2])
        if line[2*i+1] == 'O':
            ret += max(0,abs(pos - red[0]) - red[1])
            blue[1] += max(0,abs(pos - red[0]) - red[1]) + 1
            red[0] = pos
            red[1] = 0
        else:
            ret += max(0,abs(pos - blue[0]) - blue[1])
            red[1] += max(0,abs(pos - blue[0]) - blue[1]) + 1
            blue[0] = pos
            blue[1] = 0

        ret += 1

    print "Case #%d: %d" % (test+1,ret)
