#!/usr/bin/env python

from sys import stdin

T = int(stdin.readline())

for CASO in xrange(1,T+1):
    line = stdin.readline().strip().split(" ")
    C = int(line[0])
    D = int(line[C+1])
    N = int(line[C+D+2])

    combine = line[1:C+1]
    oppose = line[C+2:C+D+2]
    base = line[C+D+3]

    l = []

    for i in xrange(N):
        if len(l) == 0:
            l.append(base[i])
            continue

        combined = False
        cleared = False

        for c in combine:
            if (c[0] == base[i] and c[1] == l[-1]) or (c[1] == base[i] and c[0] == l[-1]):
                l.pop()
                l.append(c[2])
                combined = True
                break

        if combined:
            continue

        for c in oppose:
            if (c[0] == base[i] and c[1] in l) or (c[1] == base[i] and c[0] in l):
                cleared = True
                break

        if cleared:
            l = []
        else:
            l.append(base[i])

    print "Case #%d: [%s]" % (CASO, ", ".join(l))
