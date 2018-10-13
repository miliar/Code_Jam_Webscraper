#!/usr/bin/env python
# Python 2.6.4

t = int(raw_input())

for i in xrange(t):
    n, k = map(int, raw_input().split())
    m = 2**n
    print("Case #%d: %s" % (i+1, "ON" if (k % m) == (-1 % m) else "OFF"))
