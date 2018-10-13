#!/usr/bin/env python
#
# Problem: 
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from fractions import *

r = 0
l = 0
t = []
while r < 30:#r < 10**6:
    l += 2
    p = [Fraction(1)]
    r += 1
    s = [0]*l
    t.append((l, s, p))
 #   print r, p
#    r += 1
    # expansion
    s = [1]+[0]*(l-1)
    for j in range(l):
        pp = []
        for i in range(len(p)+1):
            if i == 0 or i == len(p):
                pp.append(p[0]/2)
            else:
                pp.append(p[i]/2+p[i-1]/2)
#        pp.append(Fraction(1))
        p = pp
        r += 1
        t.append((l, s, p))
        s = ([s[0]+1]+s)[:l]
 #       print r, p
    # contraction
    ps = range(l)# map(lambda x: -x, range(l))
    for j in range(l-1):
        pp = []
        for i in range(len(p)-1):
            if i == 0 or i == len(p)-2:
                pp.append(p[0]+p[1]/2)
#            elif i == len(p)-1:
#                pp.append(p[-2]+p[-1]/2)
            else:
                pp.append(p[i]/2+p[i+1]/2)
        p = pp
        r += 1
        s = map(lambda x: len(p)-x, ps)
        t.append((l, s, p))
        ps = ([0]+ps)[:l]
  #      print r, p
    p = [Fraction(1)]
    r += 1
    s = map(lambda x: len(p)-x, ps)
    t.append((l, s, p))
#    print r, p
#    print r, p
#for i in t:
#    print i



for case in range(int(raw_input())):
#    int(raw_input())
    n, x, y = map(int, raw_input().split())
#    p = [set([(0, 0)])]
    l, s, p = t[n-1]
    
  #  print n, x, y, -abs(x)+l-2, -abs(x)+l+2
#    print l, s, p
    x = abs(x)
    if y < -x + l-1: # inside core
        ans = 1.0
    #    print "."
    elif y > -x + l+1:
        ans = 0.0
    #    print "?"
    else:
   #     print "v"
#        if y > x:
#            ans = 0.0
        #else:
        try:
            ans = float(sum(p[:s[y]]))
     #           print  "K", y, s[y], p, p[:s[y]], ans
        except:
            ans = 0.0

#        ans = "ME"

    

    

#    ans = 3
    print "Case #%d: %s" % (case+1, ans)
