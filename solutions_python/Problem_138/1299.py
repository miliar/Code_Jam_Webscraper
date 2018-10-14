from __future__ import division
global Naomi,Naomi2,Ken,Ken2
def solve(N,K):
	#print("entered war")
	countN=0
	lenN=len(N)
#	print(N,K)
	while True:
#		print(N,K)		
		item=N[0]
		if item>max(K):
			K.remove(min(K))
			N=N[1:]
			countN+=1	
		else:
			for i2 in range(len(K)):
				item2=K[i2]
				if item2>item:
					K=K[:i2]+K[i2+1:]
					N=N[1:]
					break
		if N==[] or K==[]:break
	return countN		
def solveD(N,K):
	countN=0
#	print(N,K)
	maxK=max(K)
	maxN=max(N)	
	while maxK>maxN:
		K.remove(maxK)
		N.remove(min(N))
		if K==[] or N==[]:
			maxK=maxN;break
		else:
			maxK=max(K)
			maxN=max(N)
	for item in K:
		for i2 in range(len(N)):
			item2=N[i2]
			if item2>item:
				N=N[:i2]+N[i2+1:]
				countN+=1;break
	return countN
fi=open("/home/ashish/Downloads/D1.in","r")
o=open("/home/ashish/Desktop/ans/D1.txt","w")
cases=int(fi.readline().strip())
for i in range(cases):
	#solve
	n=int(fi.readline().strip())
	Naomi=[float(k) for k in fi.readline().strip().split(" ")]
	Ken=[float(k) for k in fi.readline().strip().split(" ")]
	Naomi.sort()
	Ken.sort()
	Naomi2=[a for a in Naomi]
	Ken2=[b for b in Ken]
	x=solve(Naomi,Ken)
#	print(Naomi2,Ken2)
	y=solveD(Naomi2,Ken2)
	o.write("Case #"+repr(i+1)+": %d %d\n"%(y,x))
