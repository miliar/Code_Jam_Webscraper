#!/usr/bin/env python
from collections import defaultdict

def solve(n, s, p, totals):
    if p > 10: return 0
    res = 0
    for t in totals:
        if t / 3 >= p:
            res += 1
        elif t / 3 == p-1 and t/3 > 0:
            # scores can't be negative
            # 2 possibilities
            if t % 3 == 0:
                if s:
                    res += 1
                    s -= 1
            else:
                # don't need the surprise
                res += 1
        elif t / 3 == p-2 :
            # only one way to win!
            if t % 3 == 2 and s:
                res += 1
                s -= 1
    return res



if __name__ == '__main__':
    import sys

    f = open(sys.argv[1])

    cases = int(f.readline())

    for i in xrange(cases):
        data = [int(d) for d in f.readline().strip().split()]
        n, s, p = data[:3]
        totals = data[3:]
        solution = solve(n, s, p, totals)
        print "Case #%s: %s" % (i+1, solution)

