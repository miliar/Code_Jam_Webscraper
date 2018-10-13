#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.stdin.readline()

class WillCry(Exception):
    pass

def maxpile(numbers):
    if reduce(lambda x,y:x^y, numbers, 0) != 0:
        raise WillCry
    return sum(numbers) - min(numbers)

for linenum, line in enumerate(sys.stdin):
    if linenum % 2 == 0:
        continue
    casenum = linenum / 2 + 1
    candies = map(int, line.strip().split())
    try:
        print "Case #%d: %d" % (casenum, maxpile(candies))
    except WillCry:
        print "Case #%d: NO" % casenum
