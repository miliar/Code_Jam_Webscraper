#!/usr/bin/env python

def cases(input):
    ncases = int(input.readline().strip())

    while ncases > 0:
        yield (int(input.readline().strip()),
               tuple(int(x) for x in input.readline().split()),
               tuple(int(x) for x in input.readline().split()))
        ncases -= 1

def solve(n, v1, v2):
    return sum(map(lambda (x,y): x*y, zip(sorted(v1), reversed(sorted(v2)))), 0)

if __name__ == '__main__':
    import sys

    for n, case in enumerate(cases(sys.stdin)):
        print "Case #%d: %d" % (n + 1, solve(*case))
