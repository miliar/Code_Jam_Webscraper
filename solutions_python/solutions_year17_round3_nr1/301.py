import numpy as np
import math
def mainFunc(N, K):	
	A = np.zeros(N)	
	V = np.zeros(N)
	for i in range(N):	
		P = raw_input().split(' ')
		R, H = float(P[0]),float(P[1])
		A[i] = math.pi*R*R
		V[i] = math.pi*R*2*H
	for i in range(N-K):
		mA = sorted(max(A)-A)
		maxA=mA[0]
		if(len(mA)>1): maxA=mA[1]
		lvi = A == max(A)
		V2 = np.copy(V)
		V2[lvi] += maxA
		ind = np.argmin(V2)
		V=np.delete(V,ind)
		A=np.delete(A,ind)
	x = sum(V)+max(A)
	return str(float("{0:.6f}".format(x)))
		
T = int(raw_input())
for t in range(T):
	P = raw_input().split(' ')
	print 'Case #' + str(t+1) + ': ' +	mainFunc(int(P[0]), int(P[1]))