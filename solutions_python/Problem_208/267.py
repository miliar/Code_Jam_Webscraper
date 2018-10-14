T=int(raw_input())
a=0
e=[]
while a<T:
	b=[int(x) for x in raw_input().split()]
	N=b[0]
	d=[]
	g=[]
	f=0
	while f<int(N):
		b=[int(x) for x in raw_input().split()]
		d.append(b[0])
		g.append(b[1])
		f=f+1
	f=0
	h=[]
	while f<int(N):
		b=[int(x) for x in raw_input().split()]
		h.append(b)
		f=f+1
	UV=raw_input()
	e.append([N,d,g,h])
	a=a+1

a=0
while a<T:
	b=e[a]
	N=b[0]
	d=b[1]
	g=b[2]
	h=b[3]
	i=1
	maximal=10**15
	distances=[]
	while i<=N:
		j=i+1
		array=[]
		if i<>N: S=(h[i-1])[j-1]
		while j<=N:
			if S<=d[i-1]:
				array.append(S/(g[i-1]*1.0))
			else: array.append(maximal)
			if j<>N: S=S+(h[j-1])[j]
			j=j+1
		distances.append(array)
		i=i+1
	
	D=[0] 
	E=[0]
	F=[0]
	g=1
	while g<N:
		D.append(maximal*1000)
		E.append(0)
		F.append(maximal*1000)
		g=g+1

	h=0
	while h<N:
		i=F.index(min(F))
		F[i]=maximal*1200
		j=i+1
		while j<N:
			k = D[i] + distances[i][j-i-1]
			if k < D[j]:
				D[j] = k
				E[j] = i
				if F[j] < maximal*1200:
					F[j]=k
			j=j+1
		h=h+1

	q=a+1
	r="Case #"+str(q)+": "+str(D[N-1])
	print r			
	a=a+1
	



 