#!/usr/bin/env python

from sys import stdin

def p_sum(vals):
    return reduce(lambda x,y:x^y, vals,0)

t = int(stdin.readline())
for case in xrange(1,t+1):
    num_candies = int(stdin.readline())
    candy = sorted(map(int,stdin.readline().split()))
    vals = []
    for i in xrange(1,num_candies):
        if p_sum(candy[:i]) == p_sum(candy[i:]):
            vals.append(max(sum(candy[:i]),sum(candy[i:])))
    if vals:
        print "Case #%d: %d"%(case,max(vals))
    else:
        print "Case #%d: NO"%case
