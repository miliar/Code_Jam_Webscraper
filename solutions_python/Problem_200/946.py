#!/usr/bin/env python


def solve(number):
    number = '0' + str(number)
    n = len(number)
    i = n - 1
    while i > 0 and int(number[i-1]) <= int(number[i]):
        i = i - 1
    if i == 0:
        return int(number)
    else:
        return solve(int(number[:i]) * (10**(n-i)) - 1)


T = int(raw_input().strip())
for t in range(T):
    number = raw_input().strip()
    print 'Case #%d: %s' % (t+1, solve(number))
