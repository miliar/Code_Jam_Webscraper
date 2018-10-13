#!/usr/bin/env python
#
# GCJ Problem
#
# Fair and Square

from math import sqrt
from math import pow

square_palindrome = {}

def reverse_number(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return n == reverse_number(n)

def naive_search(n):
    return is_palindrome(n) and is_palindrome(n*n)

def find_all(max):
    i = 0
    while i*i < max:
        if naive_search(i):
            square_palindrome[str(i*i)] = i
        i += 1

def print_all():
    for s,n in square_palindrome.iteritems():
        print s

def main():
    find_all(pow(10,14))
    for tc in xrange(1, int(raw_input()) + 1):
        count = 0
        n,m = [int(x) for x in raw_input().split()]
        i = 0
        for square,number in square_palindrome.iteritems():
            if int(square) >= n and int(square) <= m:
                count += 1
        print 'Case #%d: %d' % (tc, count)

if __name__ == '__main__':
    main()
