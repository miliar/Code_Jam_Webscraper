# -*- coding: utf-8 -*-

import sys

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T+1):
    op = 1
    bp = 1
    os = 0
    bs = 0
    y = 0
    line = fin.readline().split(" ")
    for i in range(1, (len(line)+1)/2):
        p = (i-1)*2
        cp = int(line[p+2])
        if line[p+1] == 'O':
            s = abs(cp - op) + 1 - bs
            op = cp
            if s < 1: s = 1
            os = os+s
            y = y + s
            bs = 0
        else:
            s = abs(cp - bp) + 1 - os
            bp = cp
            if s < 1: s = 1
            bs = bs+s
            y = y + s
            os = 0
    print "Case #%d: %d" % (case, y)

