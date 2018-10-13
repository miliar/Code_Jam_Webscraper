#!/usr/bin/env python

import sys
import gmpy


def is_fair(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_fair(s[1:-1])
        else:
            return False


def solve(A, B):
    counter = 0
    for x in range(A, B + 1):
        if is_fair(str(x)):
            if gmpy.is_square(x):
                if is_fair(str(gmpy.sqrt(x))):
                    counter += 1
    return counter


def main(infile):
    n = int(infile.readline())
    for i in range(n):
        line = infile.readline().split()
        (A, B) = map(int, line)
        print 'Case #%s: %s' % (i + 1, solve(A, B))

main(sys.stdin)
