#! /usr/bin/python

import sys


def issquare(n):
    j = n**0.5
    if j != int(j):
        return False
    return isfair(int(j))


def isfair(n):
    s = str(n)
    l = len(s)
    o = 0
    l -= 1
    while o < l:
        if s[o] != s[l]:
            return False
        o += 1
        l -= 1
    return True


t = int(sys.stdin.readline().strip())
case = 1
while case <= t:
    l = sys.stdin.readline().strip()
    ar = l.split(' ')
    a = int(ar[0])
    b = int(ar[1])

    i = a
    n = 0
    while i <= b:
        if issquare(i) and isfair(i):
            n += 1
        i += 1

    print "Case #%d: %d" % (case, n)
    case += 1
