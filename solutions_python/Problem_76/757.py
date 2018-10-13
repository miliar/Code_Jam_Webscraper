#!/usr/bin/python
import sys

if len(sys.argv) != 2:
    print 'missing argument'
    exit()

f = open(sys.argv[1], 'r')

casesTotal = int(f.readline())
caseCurrent = 1;

while caseCurrent <= casesTotal:
    n = int(f.readline().strip())
    candies = map(int, f.readline().strip().split())
    badSum = 0
    for i in candies:
        badSum = badSum ^ i
    if badSum != 0:
        print 'Case #%d: NO' % caseCurrent
    else:
        candies.remove(min(candies))
        print 'Case #%d:' % caseCurrent, sum(candies);
    caseCurrent += 1;
