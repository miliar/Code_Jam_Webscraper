#!/usr/bin/env python
import gmpy,math
import sys

f=sys.stdin
n=int(f.next())

class Case(object):
    def __init__(self):
        self.res = "IMPOSSIBLE"
        N,M,A = map(int,f.next().split())
        if N*M < A:
            return
        for xb in range(N+1):
            for yb in range(M+1):
                for xc in range(yb,N+1):
                    for yc in range(xb,M+1):

                        if abs(xb*yc - xc*yb) == A:
                            self.res = "%s %s %s %s %s %s"%(0,0,xb,yb,xc,yc)
                            return

    def run(self):
        pass

    def __str__(self):
        return str(self.res)

for case in range(1, n+1):
    c=Case()
    c.run()

    print "Case #%s: %s"%(case,c)


