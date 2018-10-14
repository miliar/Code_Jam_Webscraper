#!/usr/bin/python

import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

cases = int(raw_input())

for case in range(cases):
    data = map(int, raw_input().split())
    data.pop(0)
    data.sort()
    diff = []
    for i in range(len(data) - 1):
        diff.append( data[i + 1] - data[i] )
    while 0 in diff:
        diff.remove(0)
    gcdList = []
    for i in range(len(diff) - 1):
        gcdList.append(gcd( diff[i + 1], diff[i] ))
    if len(gcdList) == 0:
        gcdList = [diff[0]]
    T = min(gcdList)
    if T == 0:
        print data
        sys.exit(1)
    print 'Case #%d: %d' % (case + 1, (T - (data[0] % T)) % T)
