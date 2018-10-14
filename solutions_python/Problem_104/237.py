#!/usr/bin/python2
from sys import stdin

def sums(l, l1=[], l2=[]):

    if len(l1) > 0 and sum(l1) == sum(l2):
        return [l1, l2]
    if len(l) > 0:
        r = sums(l[1:], l1[:], l2[:])
        if len(r) > 0: return r

        r = sums(l[1:], l1[:]+[l[0]], l2[:])
        if len(r) > 0: return r
        r = sums(l[1:], l1[:], l2[:]+[l[0]])
        if len(r) > 0: return r
    return []
    
C = int(stdin.readline())
for c in range(1,C+1):
    l = map(int, stdin.readline().split())

    print "Case #%d:" % c
    l =  sums(l[1:])
    if len(l) == 0:
        print "Impossible"
    else:
        for n in l[0]: print n,
        print ""
        for n in l[1]: print n,
        print ""
