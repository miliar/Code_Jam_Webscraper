#!/usr/bin/python

T = input()
for i in xrange(T):
    n, k = map(int, raw_input().split())
    ans = not ((k+1) & ((1<<n) - 1))
    print 'Case #{0}: {1}'.format(i+1, ans and 'ON' or 'OFF')
