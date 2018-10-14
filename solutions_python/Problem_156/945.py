#!/usr/bin/python
# coding: utf8

import sys
from collections import Counter


def solve(diners, t=0, indent=0):
#    print " "*indent, t, diners
    max_pancakes = max(diners)
    if max_pancakes <= 3:
        return max_pancakes
    else:
        sol = 1 + solve(Counter({k-1:v for k, v in diners.iteritems()}), t+1, indent+1)
        for x in range(1, max_pancakes//2 + 1):
            diff = Counter()
            diff[max_pancakes] -= diners[max_pancakes]
            diff[max_pancakes - x] += diners[max_pancakes]
            diff[x] += diners[max_pancakes]
            sol = min(
                sol,
                diners[max_pancakes] + solve(diners + diff, t+diners[max_pancakes], indent+1),
            )
        return sol


def main():
    T = int(next(sys.stdin))
    for case in range(1, T+1):
        D = next(sys.stdin)
        diners = Counter(int(diner) for diner in next(sys.stdin).split())
#       print diners
        print "Case #{}: {}".format(case, solve(diners))


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    main()

