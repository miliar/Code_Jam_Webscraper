#!/usr/bin/python

import sys

cases = int(sys.stdin.readline())

for casenum in range(1, cases+1):
    _, aud = sys.stdin.readline().split()
    friends = 0
    standing = 0
    for i, s in enumerate(aud):
        if standing < i:
            friends += i - standing
            standing += i - standing
        standing += int(s)
    print 'Case #%s: %s' % (casenum, friends)
