#!/usr/bin/env python

import sys

def readline():
    return sys.stdin.readline().rstrip('\r\n')

def testcase():
    N = int(readline())
    array = map(int, readline().split())
    return sum((1 if value != idx+1 else 0)
        for idx, value in enumerate(array))

def main():
    n_cases = int(readline())
    for t_case in xrange(1, n_cases+1):
        print "Case #%d: %d.000000" % (t_case, testcase())

if __name__ == '__main__':
    main()

