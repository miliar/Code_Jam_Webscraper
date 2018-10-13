#!/usr/bin/python
import sys, time, collections
sys.setrecursionlimit(10096)

for caseno in range(input()):
    print >>sys.stderr, caseno
    K = input()
    z = map(int, raw_input().split())
    n = z.pop(0)
    d = z
    
    s = []
    for i in range(K, 0, -1):
        s.insert(0, i)
        #rotate
        #r = (i-1) % len(s)
        #s =  s[r:] + s[:r]
        r = (i-1) % len(s)
        s = s[-r:] + s[:-r]
        #for j in range((i-1) % len(s)):
        #    s.insert(0, s.pop())
        #print >>sys.stderr, i,r, s, z
    
    o = []
    for i in d:
        o.append( str(s[i-1]) )
    #print >>sys.stderr, s
    print "Case #%i: %s" %(caseno+1, ' '.join(o) )
