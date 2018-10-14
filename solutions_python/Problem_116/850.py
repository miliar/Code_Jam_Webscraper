from __future__ import division
import sys, string
import itertools
from math import *

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

T = int(sys.stdin.readline())

def pal(x):
    return str(x) == str(x)[::-1]

def check(M):
    for m in M:
        x = m.replace("T", "X").count('X')
        if x >= 4:
            return "X won"
        o = m.replace("T", "O").count('O')
        if o >= 4:
            return "O won"
    
    return "Game has not completed" if "." in "".join(M) else "Draw"
    
for k in range(T):
    print >> sys.stderr, k
    
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()
    C = sys.stdin.readline().strip()
    D = sys.stdin.readline().strip()
    empty = sys.stdin.readline().strip()

    cols = [A[i] + B[i] + C[i] + D[i] for i in range(4)]
    
    d1 = A[0] + B[1] + C[2] + D[3]
    d2 = A[3] + B[2] + C[1] + D[0]
    
    ans = check([A,B,C,D,d1,d2] + cols)
    
    print "Case #%d: %s" % ((k+1), ans)
