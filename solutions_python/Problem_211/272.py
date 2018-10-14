import numpy as np
def mainFunc(N, K, U):
	rStr = raw_input()+' 1'
	P = map(float,rStr.split(' '))
	P = sorted(P)
	mValue = P[0]
	qtValue = 1
	for i in range (N-K,N):
		inc = (P[i+1]-mValue)*qtValue
		if U>inc:
			qtValue+=1
			U-=inc
			mValue = P[i+1]
		else:
			mValue+=U/qtValue
			break
	for i in range (N-K,N-K+qtValue):
		P[i] = mValue
	ret = 1.0
	for i in range(N):
		ret*=P[i]
	return str(float("{0:.6f}".format(ret)))

	
T = int(raw_input())
for t in range(T):
	P = raw_input().split(' ')
	U = raw_input().split(' ')
	print 'Case #' + str(t+1) + ': '+mainFunc(int(P[0]),int(P[1]),float(U[0]))
	