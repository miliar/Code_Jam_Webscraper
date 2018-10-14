#!/usr/bin/env python

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

cases = int(raw_input())
for case in xrange(cases):
    nums = [int(x) for x in raw_input().split()][1:]
    g = 0
    for i in nums[1:]:
        g = gcd(g, abs(i - nums[0]))
    ans = (g - nums[0] % g) % g
    print 'Case #%d: %d' % (case + 1, ans)
