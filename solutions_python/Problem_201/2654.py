#!/usr/bin/env python2

import bisect
import math

import sys

def insert(gaps, gap):
    keys = [(x[1]-x[0],x[0]) for x in gaps]
    key = (gap[1]-gap[0],gap[0])
    idx = bisect.bisect_left(keys, key)
    gaps.insert(idx, gap)

def newPerson(gaps):
    gap = gaps.pop()
    insertion_point = int(math.floor((gap[1]+gap[0])/2))
    distances = []
    if gap[0] <= insertion_point -1:
        insert(gaps, (gap[0], insertion_point-1))
        distances.append(insertion_point-gap[0])
    else:
        distances.append(0)
    if gap[1] >= insertion_point +1:
        insert(gaps, (insertion_point+1, gap[1]))
        distances.append(gap[1]-insertion_point)
    else:
        distances.append(0)
    return max(*distances), min(*distances)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, k = tuple([int(x) for x in raw_input().split(' ')])
    gaps=[(0,n-1)]
    for j in xrange(k):
        a, b = newPerson(gaps)
    print "Case #{}: {} {}".format(i, a, b)
    # check out .format's specification for more formatting optionsa
