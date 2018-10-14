#! /usr/bin/env python
import sys

testcases = int(sys.stdin.readline())
case = 1
while case <= testcases:
    line = sys.stdin.readline()
    smax, order = line.split()
    smax = int(smax)
    order = [int(x) for x in list(order)]
    standing = 0
    friends = 0
    si = 0
    while si <= smax:
        s = order[si]
        if standing < si:
            nfriends = si - standing
            friends += nfriends
            standing += nfriends
        standing += s
        si += 1
    print "Case #%d: %d" % (case, friends, )
    case += 1
