#!/usr/bin/python

import sys

def time(plates, eat):
    special = sum((plate-1)/eat for plate in plates)
    return special + eat

cases = int(sys.stdin.readline())

for casenum in range(1, cases+1):
    sys.stdin.readline()
    plates = list(map(int, sys.stdin.readline().split()))
    minutes = min(time(plates, eat) for eat in range(1, 1+max(plates)))
    print 'Case #%s: %s' % (casenum, minutes)
