#! /usr/bin/env python
# -*- coding: utf-8 -*-
def recycled(a, b):
    a, b = "%d" % a, "%d" % b
    for i in xrange(1, len(a)):
        if a[i:] + a[:i] == b:
            return True

    return False

n = int(raw_input())
for i in xrange(n):
    lower, upper = raw_input().split()
    lower, upper = int(lower), int(upper)
    count = 0
    for x in xrange(lower, upper + 1):
        for y in xrange(x + 1, upper + 1):
            if recycled(x, y):
                count += 1
    print "Case #%d: %d" % (i + 1, count)
