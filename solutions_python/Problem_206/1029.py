#!/usr/bin/python

from sys import stdin

TESTCASES=int(stdin.readline().strip())

def testcase():
    a = stdin.readline().split(" ")
    D, N = int(a[0]), int(a[1])
    times = []
    for i in range(0,N):
        a = stdin.readline().split(" ")
        x, u = int(a[0]), int(a[1])
        times.append(float(D-x)/float(u))
    return "%.6f" % (float(D)/float(max(times)))

for i in range(1,TESTCASES+1):
    res = testcase()
    print "Case #%d: %s" %(i, res)

