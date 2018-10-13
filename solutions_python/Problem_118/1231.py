# -*- coding: utf-8 -*-
import math
n = raw_input()

#1,4,6,9,25

#1s1 4s4 9s9 6s6 52s25 

def p(a):
    a = str(a)
    t = True
    for i in range(0,len(a)/2+1):
        if a[i] != a[-i-1]:
            t = False
            break
    return t

for i in range(1,int(n)+1):
    s = raw_input()
    s = s.split()
    a = int(s[0])
    b = int(s[1])
    c = 0
    for j in range(int(math.sqrt(a))-1,int(math.sqrt(b))+2):
        jj = j ** 2
        if jj >= a and jj <= b and p(j) and p(jj):
            c  = c + 1
    print "Case #%d: %d" % (i,c)
