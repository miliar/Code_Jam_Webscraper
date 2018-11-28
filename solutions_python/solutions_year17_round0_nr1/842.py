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
    S, K = getWords()
    A = np.asarray([c=='-' for c in S])
    K = int(K)
    N = 0
    for i in xrange(len(A)-K+1):
        if A[i]:
            N += 1
            A[i:i+K] = ~A[i:i+K]
    res = 'IMPOSSIBLE' if A.any() else str(N)
    print "Case #%d: %s"%(caseNo, res)
