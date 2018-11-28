"""Usage:
    X.py < X.in > X.out
"""

# http://code.activestate.com/recipes/577821-integer-square-root-function/
def isqrt(x):
    "returns int(floor(sqrt(x))) using only integer math"
    assert x >= 0, 'Undefined %r' % locals()
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def is_pal(n):
    n = str(n)
    for i in range(len(n)/2+1):
        if n[i]!=n[len(n)-1-i]:
            return False
    return True

def all_fair_and_square(hl=25):
    """Off-line cache, build before downloading the large input"""
    import itertools as it
    import cPickle
    retval = set()
    for n in range(1,hl):
        for first in ['1','2']:
            for dig in it.product(['0','1'], repeat=n):
                cand = int(first+''.join(dig)+''.join(reversed(dig))+first)
                if cand <= 10**50 and is_pal(cand*cand):
                    print cand
                    retval.add(cand)
                for mid in ['0','1','2']:
                    cand = int(first+''.join(dig)+mid+''.join(reversed(dig))+first)
                    if cand <= 10**50 and is_pal(cand*cand):
                        print cand, len(str(cand))
                        retval.add(cand)
                    

    cPickle.dump(retval, open('cache.pk','w'))

    return retval


def setup(infile):
    import cPickle
    C = cPickle.load(open('cache.pk'))
    return locals()

def reader(testcase, infile, C, **ignore):
    #N = int(infile.next())
    P = map(int, infile.next().split())
    #I = map(int, infile.next().split())
    #T = infile.next().split()
    #S = [infile.next().strip() for i in range(N)]
    return locals()

def solver(infile, testcase, N=None, P=None, I=None, T=None, S=None, C=None, **ignore):
    #import collections as co
    #import functools as ft
    #import itertools as it
    #import operator as op
    #import math as ma
    #import re
    #import numpy as np
    #import scipy as sp
    #import networkx as nx
    import cPickle

    low = isqrt(P[0])
    high = isqrt(P[1])+1

    res = 0
    for i in C:
        if P[0]<=i*i<=P[1]:
            res += 1

    return 'Case #%s: %s\n' % (testcase, res)

if __name__ == '__main__':
    import sys
    T = int(sys.stdin.next())
    common = setup(sys.stdin)
    for t in xrange(1, T+1):
        sys.stdout.write(solver(**reader(t, **common)))
