import sys
import numpy as np

def getWords():
    return sys.stdin.readline().strip().split()

def getInts():
    return np.array([int(i) for i in getWords()], dtype=np.int64)

def getInt():
	i = getInts()
	assert len(i)==1
	return i[0]

#sys.stdin = open('A.in')

T = getInt()
for caseNo in xrange(1,T+1):
    D, N = getInts()
    T = 0.0 #earliest arrival time
    for i in xrange(N):
        K, S = getInts()
        T = max(T, float(D - K)/S)
    print "Case #%d: %.6f"%(caseNo, D/T)
