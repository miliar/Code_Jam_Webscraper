#!/usr/bin/env python

def palindrom(n):
    s = str(n)
    return s == s[::-1]

def count_fair_square(A, B):
    count = 0
    for n in xrange(int(A**.5), int(B**.5) + 2):
        sq = n*n
        if A <= sq <= B and palindrom(n) and palindrom(sq):
            count += 1
    return count

for i in xrange(1, int(raw_input()) + 1):
    A, B = map(int, raw_input().split())
    print "Case #%d: %d" % (i, count_fair_square(A, B))
