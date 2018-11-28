#!/usr/bin/env python

import sys

T = int(raw_input())

for t in xrange(T):
    line = raw_input().split()
    needed = 0
    curr = 0
    #print "case #%d" % (t+1)
    s = [int(x) for x in line[1]]
    for i in xrange(len(s)):
        if curr>=i:
            curr += s[i]
        elif s[i]>0:
            #print curr,i,needed
            needed += i-curr
            curr += i-curr + s[i]
    print "Case #%d: %d" % (t+1,needed)

