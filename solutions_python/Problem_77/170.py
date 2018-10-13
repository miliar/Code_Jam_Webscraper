#!/usr/bin/env python

import fileinput

def foo():
    i = iter(fileinput.input())
    i.next()
    while True:
        i.next()
        yield i.next().rstrip()

for i, nums in enumerate(foo()):
    nums = map(int, nums.split())
    res = 0
    for j, n in enumerate(nums):
        if n != j+1:
            res += 1
    print "Case #%d: %d" % (i+1, res)
