#!/usr/bin/env python

import sys

f = open(sys.argv[1])
T = int(f.readline())
for i in range(1, T + 1):
    entry = f.readline().strip().split()
    N = int(entry[0])
    Ot, Op, Bt, Bp = 0, 1, 0, 1
    for color, pos in [(entry[1 + 2 * j], int(entry[2 + 2 * j])) for j in range(N)]:
        if color == 'O':
            Ot += abs(pos - Op)
            Op = pos
            if Bt > Ot:
                Ot = Bt
            Ot += 1
        else:
            Bt += abs(pos - Bp)
            Bp = pos
            if Ot > Bt:
                Bt = Ot
            Bt += 1
    print "Case #%i:" % i, max(Ot, Bt)
f.close()
