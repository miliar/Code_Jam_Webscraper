#! /usr/bin/env python

from sys import stdin

recpairs = []
for i in range(1, 2000000):
    s = str(i)
    rec = set([int(s[j:]+s[:j]) for j in range(1, len(s))])
    recpairs.extend([(i,j) for j in rec if i<j])

ntest = input()

for test in range(ntest):
    a, b = [int(i) for i in stdin.readline().strip().split()]
    n = len([1 for i, j in recpairs if a<=i and j<=b])
    print "Case #%d: %d" % (test+1, n)