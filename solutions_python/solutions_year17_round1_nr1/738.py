import sys, string
import time
import random
import math
from copy import copy, deepcopy

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

def pm(M):
    for l in M:
        print l

def done(M):
    for l in M:
        if "?" in l:
            return False
    return True

def letters(M):
    for l in M:
        for c in l:
            if c != "?":
                yield c

def expand(M,ch,dx,dy):
    N = []
    if dx:
        for l in M:
            row = list(l)
            for i in range(len(row)):
                if row[i] == ch and not(i+dx >= 0 and i+dx < len(row) and row[i+dx] in ['?',ch]):
                    #~ print "wtf", i, i+dx, row[i], row[i+dx]
                    return False

        for l in M:
            row = list(l)
            #~ print(row,dx,len(row))
            for i in range(len(row)):
                if row[i] == ch and i+dx >= 0 and i+dx < len(row) and row[i+dx] == '?':
                    row[i+dx] = ch.lower()
            N.append(row)
    if dy:
        for l in M:
            N.append(list(l))
        for i in range(len(N)):
            for j in range(len(N[i])):
                if N[i][j] == ch and not(i+dy >= 0 and i+dy < len(N) and N[i+dy][j] in ['?',ch]):
                    return False
        for i in range(len(N)):
            for j in range(len(N[i])):
                if N[i][j] == ch and i+dy >= 0 and i+dy < len(N) and N[i+dy][j] == '?':
                    N[i+dy][j] = ch.lower()

    for i in range(len(N)):
        N[i] = ("".join(N[i])).upper()

    return N

def solve(M):
    #~ pm(M)
    #~ print
    #~ pm(expand(M,'J',-1,0))
    
    #~ pm(expand(expand(expand(M,'C',-1,0),'C', 0,1),'G',1,0))
    #~ return 0
    
    Q = [M]
    i = 0
    while i < len(Q):
        M = Q[i]
        if done(M):
            pm(M)
            return
        
        for c in letters(M):
            for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                #~ print c,dx,dy
                n = expand(M,c,dx,dy)
                if n and n not in Q:
                    #~ pm(n)
                    #~ print
                    Q.append(n)
        
        i += 1
    return "IMPOSSIBLE"

T = readint()
for t in range(T):
    R, C = readlist()
    M = []
    for i in range(R):
        row = sys.stdin.readline().strip()
        assert len(row) == C
        M.append(row)

    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1))
    solve(M)
