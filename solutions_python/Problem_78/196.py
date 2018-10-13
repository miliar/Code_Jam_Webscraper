#!/usr/bin/env python

import operator
import sys

def readline():
    return sys.stdin.readline().rstrip('\r\n')

def testcase():
    N, PD, PG = map(int, readline().split())
    if PG in (0, 100) and PD != PG:
        return False
    D = 100 / gcd(PD, 100)
    if D > N:
        return False
    return True

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def main():
    n_cases = int(readline())
    for t_case in xrange(1, n_cases+1):
        print "Case #%d: %s" % (t_case, 'Possible' if testcase() else 'Broken')

if __name__ == '__main__':
    main()
