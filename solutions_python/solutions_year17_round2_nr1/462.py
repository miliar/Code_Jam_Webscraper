import numpy as np
def mainFunc(D, N):	
	V = np.zeros(N)
	for i in range(N):	
		P = raw_input().split(' ')
		K, S = float(P[0]),float(P[1])
		V[i] = (D-K)/S
		x = round(D/max(V),6)
	return str(float("{0:.6f}".format(x)))
		
T = int(raw_input())
for t in range(T):
	P = raw_input().split(' ')
	print 'Case #' + str(t+1) + ': ' +	mainFunc(float(P[0]), int(P[1]))