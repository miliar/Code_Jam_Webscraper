import sys, string
import time
import random
import math
from copy import copy, deepcopy
from decimal import *
from mpmath import *

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

def solve(M):
    return 0

def use(U, mmap, p, s, e):
    print >> sys.stderr,  "use", p, s, e
    assert e >= s
    assert e <= 1440
    #~ print "".join(mmap[s:e])
    #~ print '.' * (e-s)
    #~ print s, e, e-s, len(mmap), len(mmap[s:e]), len('.' * (e-s))
    assert "".join(mmap[s:e]) == '.' * (e-s)
    mmap[s:e] = [p.lower()] * (e-s)
    U[p] -= e - s
    assert len(mmap) == 1440

T = readint()
for t in range(T):
    Ac, Aj = readlist()

    C = []
    J = []
    A = []
    for i in range(Ac):
        c,d = readlist()
        C.append((c,d))
        A.append((c,d,'C'))
    for i in range(Aj):
        j,k = readlist()
        J.append((j,k))
        A.append((j,k,'J'))

    #~ if t+1 != 5:
        #~ continue

    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    #~ print >> sys.stderr, C, J

    mmap = ['.'] * 60 * 24

    U = {'C': 720, 'J': 720}
    A.sort()
    off = A[0][0]
    print >> sys.stderr,  A, off
    B = [a for a in A]
    A = []
    for a in B:
        A.append((a[0]-off, a[1]-off, a[2]))
    A.append((1440, 1440, B[0][2]))
    print >> sys.stderr, A

    for s,e,p in A:
        mmap[s:e] = [p] * (e-s)
        U[p] -= (e-s)

    #~ print len(mmap)
    assert len(mmap) == 60*24
    print >> sys.stderr,  "".join(mmap)

    gapz = []
    for i in range(len(A)-1):
        a1 = A[i]
        a2 = A[i+1]
        if a1[2] != a2[2]:
            gapz.append((a2[0] - a1[1], a1, a2))
    print >> sys.stderr,  gapz

#--------------------------
    gaps = []
    for i in range(len(A)-1):
        a1 = A[i]
        a2 = A[i+1]
        if a1[2] == a2[2]:
            gaps.append((a2[0] - a1[1], a1, a2))
    print >> sys.stderr,  gaps

    N = {'C': 0, 'J': 0}
    for g in sorted(gaps):
        d, a1, a2 = g
        p = a1[2]
        #~ print p, d, a1, a2, U[p]
        if d <= U[p]:
            s, e = a1[1], a2[0]
            #~ print "need", p, s, e, e-s
            N[p] += e-s
    print >> sys.stderr,  "need:", N

    for g in sorted(gapz):
        d, a1, a2 = g
        p,q = a1[2], a2[2]
        print >> sys.stderr,  p, q, d, a1, a2, "unused", U[p], U[q], "need", N[p], N[q]
        if U[p] + U[q] >= d:
            fp, fq = 0, 0
            while fp + fq < d:
                if U[p] - N[p] - fp > U[q] - N[q] - fq:
                    fp += 1
                else:
                    fq += 1
            print >> sys.stderr, "=> ", fp, fq, d
            assert fp + fq == d
            use(U, mmap, p, a1[1], a1[1] + fp)
            use(U, mmap, q, a2[0] - fq, a2[0])

    for g in sorted(gaps):
        d, a1, a2 = g
        p = a1[2]
        print >> sys.stderr,  p, d, a1, a2, U[p]
        if d <= U[p]:
            s, e = a1[1], a2[0]
            use(U, mmap, p, s, e)

    print >> sys.stderr, "".join(mmap)

    swaps = 0
    pc = mmap[-1].upper()
    for c in mmap:
        c = c.upper()
        if c != pc:
            swaps += 1
        pc = c
    print swaps
