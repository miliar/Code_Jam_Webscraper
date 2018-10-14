#!/usr/bin/env python2

import sys

IN = sys.stdin

T = int(IN.readline().strip())

for num in range(1,T+1):
    r1 = int(IN.readline().strip())
    for i in range(4):
        if i == r1-1:
            rs1 = set(IN.readline().strip().split(' '))
        else:
            IN.readline()
    
    r2 = int(IN.readline().strip())
    for i in range(4):
        if i == r2-1:
            rs2 = set(IN.readline().strip().split(' '))
        else:
            IN.readline()

    x = rs1.intersection(rs2)

    if len(x) == 1:
        print("Case #%d: %s" % (num, list(x)[0]))
    elif len(x) == 0:
        print("Case #%d: Volunteer cheated!" % (num))
    else:
        print("Case #%d: Bad magician!" % (num))
