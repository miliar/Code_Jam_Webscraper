#!/usr/bin/env python
"""http://code.google.com/codejam/contest/dashboard?c=619102#

Two wires (a, b) and (c, d) connect if a < c and b > d.
"""

import bisect
import sys

def solve(wires):
    result = 0

    for i, (a, b) in enumerate(wires):
        for j, (c, d) in enumerate(wires[i + 1:]):
            if (a < c and b > d) or (a > c and b < d):
                result = result + 1

    return result


def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        wires = []
        for j in range(n):
            a, b = map(int, sys.stdin.readline().strip().split())
            wires.append((a, b))
        print 'Case #%d: %d' % (i + 1, solve(wires))
    return 0


if __name__ == '__main__':
    sys.exit(main())
