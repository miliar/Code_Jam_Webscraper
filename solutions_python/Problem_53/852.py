from numpy import *

filename = "A-large.in"
#filename = 'sampleA.txt'
FILE = open(filename, "r")
T = int(FILE.readline())
#print T

for k in range(T):
    L = map(int,FILE.readline().split())
    N = L[0]
    K = L[1]
    
    if K == 2**N-1:
        X = 'ON'
    else:
        X = 'OFF'
    if (K+1)%(2**N) == 0:
        X = 'ON'

    print 'Case #%d: %s'%(k+1,X)

'''
    for n in range(2,K):
        if K+1%(2**(N-1))==0:
            print K+1, n, n*(2**(N-1))
            X = 'ON'
'''
   

'''
    O = zeros(len(N))
    P = zeros(len(N))
    for j in range(len(N)):
    	O[j] = false
    	P[j] = false
    P[0] = true
    for i in range(K):
    	if (P[i] == 1):
            O[i] = (O[i]+1)/2
#			if (O[i] == 1):
#				O[i] == 0;
#			if (O[i] == 0):
#		if (P[i] == 1) and (O[i] == 0):
#			O[i] == 1;
'''
