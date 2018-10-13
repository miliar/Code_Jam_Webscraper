import sys, string
import time

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

T = readint()
for t in range(T):
    N = readint()
    P = readlist()
    
    #~ if t != 3: continue
    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    
    X = []
    for i in range(N):
        X.append([chr(ord('A')+i), P[i]])
    #~ print X
    
    total = sum(P)
    #~ print total

    Out = ""
    while total > 0:
    #~ for k in range(10):
        X.sort(key=lambda x: -x[1])
        out = ""
        if X[0][1]:
            out += X[0][0];
            X[0][1] -= 1
            total -= 1
        
        M = max(X, key=lambda x: x[1])
        ok = M[1] <= total/2.0
        
        if ok:
            Out += out + ' '
        else:
            Out += out
        
        #~ print out, X, ok
    print Out
        
