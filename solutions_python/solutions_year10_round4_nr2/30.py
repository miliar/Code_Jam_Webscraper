

import sys
stin = sys.stdin

t = int(stin.readline())
for tcase in range(t):
    p = int(stin.readline())
    constraints = map(int, stin.readline().split())

    for i in range(p):
        stin.readline()

    levels = range(p)
    for i in range(p):
        levels[i] = [False] * (1 << i)

    for pos, c in enumerate(constraints):
        if c == p:
            continue
        for i in range(c):
            pos /= 2
        for i in range(p - c):
            pos /= 2
            levels[p-1 -(c+i)][pos] = True

    cost = 0
    for lev in range(len(levels)):
        for i in range(len(levels[lev])):
            if levels[lev][i]:
                cost += 1

    print "Case #%d:" % (tcase+1), cost
