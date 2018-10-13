#!/usr/bin/env python

import sys

inp = sys.stdin
oup = sys.stdout

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    if b > a:
        tmp = a
        a = b
        b = tmp
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a

C = int(inp.readline())
for case in range(1, C+1):
    nums = [int(x) for x in inp.readline().split()]
    assert nums[0] == len(nums)-1
    N = nums.pop(0)

    nums.sort()
    # Differentiate list.
    diffs = []
    for i in xrange(N-1):
        diffs.append(nums[i+1] - nums[i])
    # Find gcd.
    g = diffs[0]
    for i in xrange(1, len(diffs)):
        g = gcd(g, diffs[i])

    if nums[0] % g == 0:
        apocalypse = 0
    else:
        apocalypse = g - (nums[0] % g)
    print "Case #%d: %d" % (case, apocalypse)

