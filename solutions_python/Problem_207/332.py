import sys, string
import time
import random
import math
from copy import copy, deepcopy

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

def solve(M):
    return 0

def reorder(inp, N):
    ring = ""
    Q = [x for x in inp]
    R = []
    i = 0
    prev_len = N
    while len(ring) < N:
        for c in Q:
            if len(ring) == 0 or \
              (len(ring) < N-1 and c != ring[-1]) or \
              (len(ring) == N-1 and c != ring[-1] and c != ring[0]):
                ring += c
            else:
                R.append(c)
        #~ print ring + ("?" * (N - len(ring))), len(R)
        
        #~ print "".join(R)
        #~ print len(R)
        if len(R) == prev_len:
            #~ print >> sys.stderr, "no progress", len(R)
            break
        prev_len = len(R)
        random.shuffle(R)
        R.sort(key=lambda x: 0 if x==ring[0] else 1)
        Q = [x for x in R]
        R = []

    if len(ring) == N:
        return ring

    return None

def fits(ring, c):
    if len(ring) == 0 or \
      (len(ring) < N-1 and c != ring[-1]) or \
      (len(ring) == N-1 and c != ring[-1] and c != ring[0]):
        return True
    return False

def tryx(L):
    a,x = L[0]
    b,y = L[1]
    c,z = L[2]
    
    ring = ""
    
    print >> sys.stderr, ring, a, b, c
    for i in range(a):
        if c and fits(ring, z):
            ring += z
            c -= 1
        if a and fits(ring, x):
            ring += x
            a -= 1
    #~ print >> sys.stderr, ring, a, b, c

    for i in range(b):
        if b and fits(ring, y):
            ring += y
            b -= 1
        if c and fits(ring, z):
            ring += z
            c -= 1
    #~ print >> sys.stderr, ring, a, b, c
    #~ print >> sys.stderr, len(ring), N

    if len(ring) == N:
        return ring
    else:
        return None


def tryy(L):
    ring = ""

    for i in range(N):
        L.sort(key=lambda x: x[0])
        if L[2][0] and fits(ring, L[2][1]):
            ring += L[2][1]
            L[2] = (L[2][0]-1, L[2][1])
        elif L[1][0] and ring[0] == L[1][1] and fits(ring, L[1][1]):
            ring += L[1][1]
            L[1] = (L[1][0]-1, L[1][1])
        elif L[0][0] and ring[0] == L[0][1] and fits(ring, L[0][1]):
            ring += L[0][1]
            L[0] = (L[0][0]-1, L[0][1])
        elif L[1][0] and fits(ring, L[1][1]):
            ring += L[1][1]
            L[1] = (L[1][0]-1, L[1][1])
        elif L[0][0] and fits(ring, L[0][1]):
            ring += L[0][1]
            L[0] = (L[0][0]-1, L[0][1])
        else:
            pass
            #~ print >> sys.stderr, "wtf"
        #~ print ring, L
    #~ print L

    if len(ring) == N:
        return ring
    else:
        return None

T = readint()
for t in range(T):
    L = readlist()
    N = L[0]
    R, O, Y, G, B, V = L[1:]
    assert sum(L[1:]) == N

    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),

    inp = "R" * R + "O" * O + "Y" * Y + "G" * G + "B" * B + "V" * V

    L = [(R,'R'), (B,'B'), (Y,'Y')]
    L.sort(key=lambda x: x[0])

    sol = tryx(L)
    if sol:
        assert len(sol) == N
        print sol
        continue
    print >> sys.stderr, "IMPOSSIBLE?"

    sol = tryy(L)
    if sol:
        print sol
        continue
    print >> sys.stderr, "IMPOSSIBLE?"

    print >> sys.stderr, "IMPOSSIBLE!"
    print "IMPOSSIBLE"
