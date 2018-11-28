import math

for L in range(int(input())):
	N,K = [t(s) for t,s in zip((int,int),input().split())]
	U = float(input())
	P = [float(x) for x in input().split()]
	
	while U:
		P = sorted(P)
		
		neq = 0
		while neq < len(P) and P[neq]==P[0]:
			neq+=1
		
		if len(P)==neq: cost = U
		else: cost = (P[neq]-P[0])*neq
		#print(cost,neq,P,U)
		if cost < U:
			for i in range(neq):
				P[i] = P[neq]
			if P[0]!=P[neq]: 1/0
			U -= cost
		else:
			for i in range(neq):
				P[i] += U/neq
			U = 0
	
	prod = 1
	for p in P:
		prod *= p
	print("Case #"+str(L+1)+": "+str(prod))










