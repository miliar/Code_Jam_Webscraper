#!/usr/bin/python

import sys

def combine(n):
    return n * (n-1) / 2

def check_num(a, b, x):
    xstr = str(x)
    results = set()
    results.add(x)
    for i in xrange(len(xstr)):
        xstr = xstr[-1] + xstr[:-1]
        if xstr[0] == '0':
            continue
        y = int(xstr)
        if y < a or y > b:
            continue
        if y > x:
            return 0
        results.add(y)
    return len(results)

def cal(a, b):
    result = 0
    for x in xrange(a, b+1):
        result += combine(check_num(a, b, x))
    return result

cases = sys.stdin.readline()
n = int(cases)
for i in xrange(1, n+1):
    line = sys.stdin.readline()
    fields = line.split()
    a = int(fields[0])
    b = int(fields[1])
    print "Case #%d: %d" % (i, cal(a, b))
