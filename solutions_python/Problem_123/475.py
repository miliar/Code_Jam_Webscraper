#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
d = {}
def solve(a, s, i = 0):
    #if (a, i) in d:
    #    return d[(a, i)]
    while len(s) > i:
        if s[i] < a:
            a = a + s[i]
            i += 1
        else:
            a_ = a

            t1 = 10*99
            if a > 1:
                t1 = 0
                while a_ <= s[i]:
                    t1 += 1
                    a_ = 2 * a_ - 1
                #print a_, s
                tmp1 = solve(a_, s, i)
                t1 += tmp1
            tmp2 = solve(a, s, i + 1)
            t2 = 1 + tmp2
            
            if t1 < t2:
                d[(a_,  i)] = tmp1
                return t1
            else:
                d[(a, i + 1)] = tmp2
                return t2
            
            break
    return 0
        

C = int(sys.stdin.readline())
for c in range(1,C+1):
    a, n = map(int, sys.stdin.readline().split())
    l = sorted(map(int, sys.stdin.readline().split()))
    res = 0
    
        
    print "Case #%d: %d" % (c , solve(a, l))
