#!/usr/bin/env python

from math import *

def doit():
    n = input()
    # generate by PARI-gp
    # f(x) = (3+sqrt(5))^x
    # g(x) = floor(f(x)) % 1000
    ans = [1 ,5 ,27 ,143 ,751 ,935 ,607 ,903 ,991 ,335 ,47 ,943 ,471 ,55 ,447 ,463 ,991 ,95 ,607 ,263 ,151 ,855 ,527 ,743 ,351 ,135 ,407 ,903 ,791 ,135 ,647]
    return ans[n]

n = input()
for x in xrange(n):
    print 'Case #%d: %03d' % (x + 1, doit())
