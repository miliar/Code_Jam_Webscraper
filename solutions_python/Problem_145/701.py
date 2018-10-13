
from itertools import *
import sys
from fractions import gcd

debug = False

def log(*argv):
    if debug:
        print " ".join(imap(str, argv))

def ans(case, *argv):
    print "Case #" + str(case) + ":", " ".join(imap(str,argv))

def main(f, case):
    P,Q = map(int, f.readline().split("/"))
    log(P, Q)
    if Q > 2 and Q%4 != 0:
        ans(case, "impossible")
        return
    p = P
    q = Q/2
    n = 1
    while p > 1 and q > 1:
        g = gcd(p,q)
        if g != 1:
            p /= g
            q /= g
        else:
            break
    log(p, q)
    while 1 < q:
        if q % 2 != 0:
            ans(case, "impossible")
            return
        if p < q:
            n += 1
        q = q/2
        #if p > 1:
        #    p = p/2
    ans(case, n)

with open(sys.argv[1]) as f:
    N = int(f.readline())
    for i in xrange(N):
        main(f, i+1)
