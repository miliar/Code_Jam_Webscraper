#!/usr/bin/env python
import sys
import bisect
from decimal import Decimal


def find_gt(a, x):
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]


def all_bigger(a, b):
    for x in range(len(a)):
        if a[x] < b[x]:
            return False
    return True


inp = open(sys.argv[1], 'r')
out = open('outd.txt', 'w')
cases = inp.readline()
for i in range(int(cases)):
    n = int(inp.readline())
    naomi = sorted([Decimal(x) for x in inp.readline().split()])
    ken = sorted([Decimal(x) for x in inp.readline().split()])
    ken2 = ken[:]
    wins = 0
    deceitful_wins = 0
    for x in naomi:
        # Normal war
        if max(ken) < x:
            ken.pop(0)
            wins += 1
        else:
            ken.remove(find_gt(ken, x))
    # Deceitful war
    for k in range(n):
        if all_bigger(naomi, ken2):
            deceitful_wins += len(naomi)
            break
        else:
            naomi.pop(0)
            ken2.pop()
    out.write('Case #' + str(i + 1) + ': ' + str(deceitful_wins)
              + ' ' + str(wins) + '\n')
