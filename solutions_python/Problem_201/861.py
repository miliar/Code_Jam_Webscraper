import sys
#import numpy as np

def getWords():
    return sys.stdin.readline().strip().split()

def getInts():
    return [int(i) for i in getWords()]

def getInt():
	i = getInts()
	assert len(i)==1
	return i[0]

#sys.stdin = open('C.in')

T = getInt()
for caseNo in xrange(1,T+1):
    N, K = getInts()
    
    n = N
    l = 1
    m = 0
    k = 0
    
    while k + l + m < K:
        #print n, l, m, k
        #print [n]*l + [n-1]*m
        k += l+m
        (n, l, m) = (n//2, l + (n%2)*(l+m), m + (1-n%2)*(l+m))
    
    if k + l < K:
        r0, r1 = (n-1)//2, (n-2)//2
    else:
        r0, r1 = n//2, (n-1)//2
    print "Case #%d: %d %d"%(caseNo, r0, r1)
