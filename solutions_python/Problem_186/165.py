import sys, string
import time
import random

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

def try_fake(S):
    Ax = set()
    Bx = set()
    fake = 0
    for a,b,s in S:
        if a in Ax and b in Bx:
            fake += 1
        else:
            Ax.add(a)
            Bx.add(b)
    return fake

T = readint()
for t in range(T):
    N = readint()
    A = []
    B = []
    for i in range(N):
        s = sys.stdin.readline().strip()
        a,b = s.split(" ")
        A.append(a)
        B.append(b)
    
    #~ if t != 3: continue
    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    
    S = []
    for i in range(N):
        S.append([A[i], B[i], 0])

    best = 0
    for k in range(10000):
        for i in range(N):
            a = S[i][0]
            b = S[i][1]
            S[i][2] = random.random()
            #~ if k == 0:
                #~ S[i][2] = min(A.count(a), B.count(b))
            #~ elif k == 1:
                #~ S[i][2] = min(A.count(a), B.count(b)) + max(A.count(b), B.count(b)) * 1e-5
            #~ elif k == 3:
                #~ S[i][2] = min(A.count(a), B.count(b)) - max(A.count(b), B.count(b)) * 1e-5
            #~ else:

        S.sort(key=lambda x: x[2])
        #~ print S
        x = try_fake(S)
        if x > best:
            best = x
    Au = set(A)
    Bu = set(B)
    print best#, N - max(len(Au),len(Bu))

