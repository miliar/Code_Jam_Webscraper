#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tidy_number(n):
    t = list(str(n))
    for i in range(len(t)-1):
        if t[i] <= t[i+1]: continue
        t = t[:i+1] + ['0']*(len(t)-i-1)
        return int(''.join(t)) - 1
    return int(''.join(t))

def solve(N):
    tn = 0
    while N != tn:
        tn = N
        N = tidy_number(N)

    return tidy_number(N)

if __name__ == "__main__":
    test_cases = input()

    for i in xrange(1, test_cases+1):
        N = raw_input()
        print "Case #{}: {}".format(i, solve(int(N)))
