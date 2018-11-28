from __future__ import division
import sys
sys.setrecursionlimit(10000)
# cookie clicker
EXAMPLE_IN = """\
4
4 11111
1 09
5 110011
0 1"""

EXAMPLE_OUT = """\
Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0
"""


def solve(shynesses):
    guests = 0
    tot = 0
    for i in range(len(shynesses)):
        if i > tot:
            guests += i - tot
            tot = i
        tot += shynesses[i]
    return guests


def main(lines):
    for i in xrange(int(next(lines))):
        shynesses = map(int, next(lines).strip().split(' ')[1])

        ans = 'Case #%d: %s' % (i+1, solve(shynesses))
        print ans




if __name__ == '__main__':
    if len(sys.argv) == 1:
        input = iter(EXAMPLE_IN.split('\n'))
    else:
        input = open(sys.argv[1])
    main(input)
