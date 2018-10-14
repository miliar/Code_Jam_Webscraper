import sys, string
from copy import copy, deepcopy
import gmpy
import time

import sys
sys.setrecursionlimit(1000000)

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readbinlist():
	return [int(x,2) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

T = readint()

def solve(S,X):
    
    if len(S) == 0:
        return 0
    
    sol = 1 + solve(S[1:], X)
    
    for i in range(1,len(S)):
        if S[0] + S[i] <= X:
            tryx = 1 + solve(S[1:i] + S[i+1:], X)
            sol = min(sol, tryx)
    return sol

def qsolve(S,X):

    if len(S) == 0:
        return 0
    
    for i in range(1,len(S)):
        if S[0] + S[i] <= X:
            return 1 + qsolve(S[1:i] + S[i+1:], X)

    return 1 + qsolve(S[1:], X)


for t in range(T):
    N,X = readlist()
    S = readlist()
    
    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    S.sort(reverse=True)

    print qsolve(S,X)
