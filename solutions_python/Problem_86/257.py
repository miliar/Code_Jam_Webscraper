#!/usr/bin/python
import sys

def doit(L,H,O):
    for n in xrange(L,H+1):
        h = True
        for o in O:
            if harmony(n,o)==False:
                h=False
                break
        if h==True:
            return n

    return "NO"

def harmony(a,b):
    if (a/b)*b==a: return True
    if (b/a)*a==b: return True
    return False

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        N,L,H = map(int, f.readline().split())
        O = map(int, f.readline().split())

        nn = doit(L,H,O)

        print "Case #%d:" % (_t+1), nn
