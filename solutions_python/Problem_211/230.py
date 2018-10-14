t=int(input())
for i in range(1,t+1):
	N,K=[int (s) for s in input().split(" ")]
	U=float(input())
	P=[float(s) for s in input().split(" ")]
	P.sort()
	while U>0:
		minp=P[0]
		cti=1
		for j in range(1,len(P)):
			if P[0]==P[j]:
				cti+=1
		if cti==len(P):
			for j in range(0,len(P)):
				P[j]=P[j]+U/len(P)
			U=0
		else:
			improvement=P[cti]-P[0]
			#print(improvement)
			if improvement*cti<U:
				for j in range(0,cti):
					P[j]=P[j]+improvement
					U=U-improvement
			else:
				improvement=U/cti
				U=0
				for j in range(0,cti):
					P[j]=P[j]+improvement
		#print(P)
	prob=1
	for j in range(0,N):
		prob=prob*P[j]
	print("Case #{}: {}".format(i,prob))