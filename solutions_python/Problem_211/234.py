import numpy as np

def p3(U,Pi):
	avg = sum(Pi) + U
	avg /= len(Pi)
	
	tot = 0
	nb = 0
	prob = 1.
	for i in range(len(Pi)):
		if Pi[i] < avg:
			tot += Pi[i]
			nb += 1
		else:
			prob *= Pi[i]
			
	if nb > 0:
		prob *= ((tot+U)/nb)**nb
	
	return prob
	
	
	

T = int(input())
for t in range(T):
	K,N = input().split()
	K,N = int(K), int(N)
	U = float(input())
	Pi = list(map(float, input().split() ))

	
	
	print("Case #%d: %f"%(t+1,p3(U,Pi)))
