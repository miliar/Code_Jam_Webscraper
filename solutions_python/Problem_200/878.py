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

#sys.stdin = open('B.in')

T = getInt()
for caseNo in xrange(1,T+1):
    N = [int(c) for c in getWords()[0]]
    L = len(N)
    i = 0
    while i < L-1 and N[i+1]>=N[i]:
            i += 1
    if i < L-1:
        while i>0 and N[i-1] == N[i]:
            i -= 1
        N[i] -= 1
        for j in xrange(i+1, L):
            N[j] = 9
    print "Case #%d: %d"%(caseNo, int(''.join([str(d) for d in N])))
