#! /usr/bin/python3.1

import sys
from sys import stdin
import os
import fractions

def solve(n, *ti):
    ti = list(ti)
    ti.sort()
    recent = last = ti[0]
    diffs = []
    for t in ti[1:]:
        diffs.append(t - last)
        last = t
    while len(diffs) > 1:
        a = diffs.pop(0)
        diffs[0] = fractions.gcd(a, diffs[0])
    capt = diffs[0]
    y = capt - recent
    while y < 0:
        y += capt
    return y

def main(argv=sys.argv):
    ncases = int(stdin.readline().strip())
    for i in range(1, ncases + 1):
        case = [int(x) for x in stdin.readline().split()]
        print("Case #{0}: {1}".format(i, solve(*case)))
    return 0

if __name__ == '__main__':
    sys.exit(main())
