from __future__ import division

import sys
sys.setrecursionlimit(10000)
# cookie clicker
EXAMPLE_IN = """\
5
3 4 2
4 5 2
7 8 5
45 56 35
103 143 88
"""

EXAMPLE_OUT = """\
Case #1: 10
Case #2: 16
Case #3: 52
Case #4: 2411
Case #5: 14377
"""


def solve(a, b, k):
    a, b = sorted([a,b])
    tot = 0
    for the_a in xrange(a):
        for the_b in xrange(b):
            if the_a & the_b < k:
                tot+=1
    return tot


def main(lines):
    for i in xrange(int(next(lines))):
        a, b, k = map(int, next(lines).split())
        ans = 'Case #%d: %s' % (i+1, solve(a, b, k))
        print ans




if __name__ == '__main__':
    if len(sys.argv) == 1:
        input = iter(EXAMPLE_IN.split('\n'))
        print 'Should be', EXAMPLE_OUT
    else:
        input = open(sys.argv[1])
    main(input)
