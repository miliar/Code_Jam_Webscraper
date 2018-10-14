#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import log10

def solve(n):
    nd = int(log10(n)) + 1

    digits = []
    for i in xrange(nd):
        x = 10 ** (nd - i)
        t = n / x
        digits.append(t)
        n = n % x
    digits.append(n % 10)

    digits.reverse()

    for i in xrange(nd-1):
        if digits[i] == -1:
            digits[i] = 9
            digits[i+1] = digits[i+1] - 1
        if digits[i] < digits[i+1] or digits[i] == 0 or digits[i+1] == 0:
            for j in xrange(i+1):
                digits[i-j] = 9
            digits[i+1] = digits[i+1] - 1

    if digits[nd-1] == -1:
        digits[nd-1] = 0
    x = 0
    for i in xrange(nd):
        x = x + digits[i] * 10**i

    return x

def main():
    T = int(raw_input())
    for i in xrange(T):
        N = int(raw_input())
        print 'Case #{}: {}'.format(i + 1, solve(N))

if __name__ == '__main__':
    main()
