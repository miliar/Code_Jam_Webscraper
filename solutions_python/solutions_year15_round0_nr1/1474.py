#!/usr/bin/env python
# encoding: utf-8
"""
" Problem A in quialification round of google codejam 2015
" Author: Tsirif
"""

T = int(raw_input())
for i in xrange(1,T+1):
    nFriends = 0
    SMax, aud = raw_input().split()
    SMax = int(SMax)
    aud = map(int, list(aud))

    for j in xrange(len(aud)):
        # print
        # print str(aud[j])+" "+str(j)
        # print "nFr "+str(nFriends)
        # print "total applaud "+str(aud[j-1] + nFriends)
        if j == 0:
            # print "skip"
            continue
        if aud[j] == 0:
            aud[j] += aud[j-1]
            # print "skip"
            continue
        total_applauding = aud[j-1] + nFriends
        if j > total_applauding:
            nFriends += (j - total_applauding)
        aud[j] += aud[j-1]

    print "Case #"+str(i)+": "+str(nFriends)
