#!/usr/bin/env python
import gmpy
import sys

gmpy.set_minprec(20000)

f=sys.stdin
t=int(f.next())

    
for case in range(1, t+1):
    n = int(f.next())
    s = 3+gmpy.fsqrt(5)
    res = long(s**n)
    print "Case #%s: %s"%(case,str(res)[-3:].rjust(3,'0'))


