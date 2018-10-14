#!/usr/bin/env python

import sys

def is_palindrome(n):
    nstr = str(n)
    return nstr == ''.join(reversed(nstr))

def main():
    T = int(sys.stdin.readline())
    pali_and_sqr = []
    for n in xrange(1, 10**7):
        if is_palindrome(n) and is_palindrome(n*n):
            pali_and_sqr.append(n*n)
    for test_case in xrange(T):
        A, B = map(int, sys.stdin.readline().split())

        count = len(filter(lambda x: A <= x <= B, pali_and_sqr))

        print "Case #%d: %d" % (test_case+1, count)

if __name__ == '__main__':
    main()
