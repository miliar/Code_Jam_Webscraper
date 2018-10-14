#! /usr/bin/env python

from math import factorial as f, sqrt

for tc in xrange(1,input()+1):
    s,k = raw_input().split()
    s,k = list(s),int(k)
    res = 0
    for i in xrange(len(s)-k+1):
        if s[i]=='-':
            for j in xrange(i,i+k):
                s[j] = '+' if s[j]=='-' else '-'
            res += 1
    if '-' in s:
        print "Case #%d: IMPOSSIBLE"%(tc)
    else:
        print "Case #%d: %d"%(tc,res)

