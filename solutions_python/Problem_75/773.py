#!/usr/bin/env python

import sys

line = sys.stdin.readline()
nbCase = int(line)
for noCase in xrange( 1, nbCase + 1 ):
    line = sys.stdin.readline()
    line = line.split()
    comb = []
    for i in xrange(int(line.pop(0))):
        comb.append(line.pop(0))
    opp = []
    for i in xrange(int(line.pop(0))):
        opp.append(line.pop(0))

    r = []
    for i in xrange(int(line.pop(0))):
        r.append(line[0][i])
        b = False
        for c in comb:
            try:
                if (r[-1] == c[0] and r[-2] == c[1]) or \
                        (r[-2] == c[0] and r[-1] == c[1]):
                    del r[-2:]
                    r.append(c[2])
                    b = True
                    break
            except IndexError:
                pass

        if not b:
            for o in opp:
                if (r[-1] == o[0] and o[1] in r) or \
                        (r[-1] == o[1] and o[0] in r):
                    r = []
                    break

    print 'Case #' + str(noCase) + ': ' + str(r)
