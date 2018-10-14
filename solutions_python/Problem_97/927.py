#!/usr/bin/python

# usage ./p3.py <input file>

import sys


def get_arrangements(n):
    sn = str(n)
    ln = len(sn)
    r = []
    for i in xrange(ln):
        rearr = int(sn[i:] + sn[0:i])
        if len(str(rearr)) == ln:
            r.append(rearr)
    return list(set(r))


def rec_count(n, mx):
    arr = get_arrangements(n)
    count = 0
    for i in arr:
        if i>n and i<=mx:
            count += 1
    return count

def getrangecount(A,B):
    c = 0
    for i in xrange(A,B):
        c += rec_count(i, B)
    return c

lines = open(sys.argv[1]).read().split("\n")

i=0

for line in lines[1:-1]:
    i += 1
    nums = line.split(" ")
    a = []
    for num in nums:
        a.append(int(num))
    print "Case #%d:" % i, getrangecount(a[0],a[1])


#for num in (12345, 234, 1, 12, 105):
#    print get_arrangements(num)
