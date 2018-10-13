from codejam import *
from fractions import gcd

def run(f):
    n=int(f.next())
    ts=[int(f.next()) for i in range(n)]
    ts.sort()
    ps=[ts[i+1]-ts[i] for i in range(n-1)]
    mgcd = reduce(gcd, ps, ps[0])
    print (-ts[0])%mgcd
    assert (-ts[0])%mgcd==(-ts[1])%mgcd
    return

def main(fn):
    f=Reader(fn)
    n=int(f.next())
    for i in range(n):
        print 'Case #%d:'%(i+1), #TODO
        run(f)
    return

import sys
main(*sys.argv[1:])
