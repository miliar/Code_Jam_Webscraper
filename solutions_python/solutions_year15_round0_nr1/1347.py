#!/usr/bin/python

import sys

T = int(sys.stdin.readline())

for t in range(T):
    SMAX, S = sys.stdin.readline().split()
    SMAX = int(SMAX)
    total = 0
    friends = 0
    for k in range(SMAX+1):
        Si = int(S[k])
        additionFriends = max(0, k - total)
        total += Si + additionFriends
        friends += additionFriends
        
    print "Case #%d: %d" % (t+1, friends)
