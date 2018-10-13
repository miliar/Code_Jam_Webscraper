#!/usr/bin/env python

import sys

sys.setrecursionlimit(32500)

def proc(l, p, c):
    if l * c >= p:
        return 0
    else:
        l1 = l
        p1 = p
        while l1 < p1:
            l1 *= c
            p1 /= c
        return 1 + max([proc(round((l1+p1)/2.0), p, c), proc(l, (l1+p1)/2, c)])

if __name__ == '__main__':
    test_cases = int(raw_input())
    
    for case in xrange(1, test_cases+1):
        l, p, c = map(int, raw_input().split(' '))
        
        print "Case #%d: %d" % (case, proc(l,p,c))
        
        