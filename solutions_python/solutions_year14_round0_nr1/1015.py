#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


#file = open("/Users/flynn/playground/gcj/qualification/a.input", 'r')
file = sys.stdin

def read_case():
    r = int(file.readline())
    nums = [map(int, file.readline().split()) for i in range(4)]
    return set(nums[r - 1])

T = int(file.readline())

for t in xrange(T):
    r1 = read_case()
    r2 = read_case()
    common = list(r1 & r2)
    print "Case #%s:" % (t+1),
    if len(common) == 1:
        print common[0]
    elif len(common) > 1:
        print "Bad magician!"
    else:
        print "Volunteer cheated!"

