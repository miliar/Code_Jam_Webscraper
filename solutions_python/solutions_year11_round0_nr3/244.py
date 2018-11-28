#!/usr/bin/env python

import operator
import sys

def readline():
    return sys.stdin.readline().rstrip('\r\n')

def testcase():
    N = int(readline())
    C = map(int, readline().split())
    if reduce(operator.xor, C) != 0:
        return 'NO'
    else:
        return sum(C) - min(C)

def main():
    n_cases = int(readline())
    for t_case in xrange(1, n_cases+1):
        print "Case #%d: %s" % (t_case, testcase())

if __name__ == '__main__':
    main()
