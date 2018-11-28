import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall

def getWords():
    return sys.stdin.readline().strip().split()

def getInts():
    return np.array([int(i) for i in getWords()], dtype=np.int64)

def getInt():
	i = getInts()
	assert len(i)==1
	return i[0]

#sys.stdin = open('C.in')

T = getInt()
for caseNo in xrange(1,T+1):
    N, Q = getInts()

    ES = []
    for i in xrange(N):
        ES.append(getInts())
    ES = np.asarray(ES)

    D = []
    for i in xrange(N):
        D.append(getInts())
    D = np.asarray(D, dtype=float)
    D[D==-1]=np.inf

    L = floyd_warshall(D)
    T = floyd_warshall(np.choose(L <= ES[:,:1], [np.inf, L/ES[:,1:]]))

    res = []
    for i in xrange(Q):
        u,v = getInts()-1
        res.append(T[u,v])
    res = tuple(res)
    print ("Case #%d:"+" %.7f"*Q)%((caseNo,)+res)

