T=raw_input()

N=[]
M=[]
for i in range(int(T)):
	NN=raw_input()
	naomi=raw_input()
	ken  =raw_input()
	
	n   = [float(i) for i in naomi.split()]
	nnn = [float(i) for i in naomi.split()]
	k   = [float(i) for i in ken.split()]
	kkk = [float(i) for i in ken.split()]
	N.append([n,k])
	M.append([nnn,kkk])

def war(X,Y):
	X.sort()
	wn=0
	for i in range(len(Y)):
		Z=filter(lambda x: x>Y[i],X)
		if len(Z)<1:
			wn+=1
			X.remove(min(X))
		else:
			X.remove(min(Z))
	return wn	

def taquito(X,Y):
	for i in range(len(X)):	
		if X[i]<Y[i]:
			return False
	return True
def naomiwar(X,Y):
	X.sort()
	Y.sort()
	R=taquito(X,Y)
	while R==False:
		X.remove(min(X))
		Y.remove(max(Y))
		R=taquito(X,Y)
	return len(X)
for j in range(len(N)):
	A=N[j][0]
	B=N[j][1]
	P=M[j][0]
	Q=M[j][1]
	print 'Case #%i: %i %i' %(j+1, naomiwar(P,Q), war(B,A))
