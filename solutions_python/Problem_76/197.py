#! /usr/bin/env python
import sys
from operator import xor

def main():
    t = int(raw_input())
    for i in xrange(t):
        n = int(raw_input())
        candy = map(int, raw_input().split())
        assert len(candy) == n
        print 'Case #%d:' % (i + 1), solve(candy)

def botcode(c):
    return 0 if c == 'O' else 1

def solve(candy):
    if reduce(xor, candy) != 0:
        return 'NO'
    return sum(candy) - min(candy)


if __name__ == '__main__':
    sys.exit(main())
