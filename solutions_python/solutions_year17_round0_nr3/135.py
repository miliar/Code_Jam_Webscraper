import numpy as np
def mainFunc(N, K):
	L = 0
	R = 0
	D = {N:1}
	j = 0
	while j<K:
		v = max(D.keys())
		L = (v-1)/2
		R = v/2
		if L in D.keys(): D[L]+=D[v]
		else: D[L]=D[v]
		if R in D.keys(): D[R]+=D[v]
		else: D[R]=D[v]
		j+=D[v]
		del D[v]
	return str(R)+" "+str(L)

T = int(raw_input())
for t in range(T):
	P = raw_input().split(' ')
	print 'Case #' + str(t+1) + ': '+mainFunc(int(P[0]),int(P[1]))
	