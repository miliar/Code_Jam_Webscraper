T=int(raw_input())
a=0
e=[]
while a<T:
	b=[int(x) for x in raw_input().split()]
	D=b[0]
	N=b[1]
	d=[]
	g=[]
	f=0
	while f<int(N):
		b=[int(x) for x in raw_input().split()]
		d.append(b[0])
		g.append(b[1])
		f=f+1
	e.append([D,N,d,g])
	a=a+1

a=0
while a<T:
	h=e[a]
	D=h[0]
	N=int(h[1])
	K=h[2]
	S=h[3]
	i=1
	v=S[0]/(1-K[0]/(D*1.0))
	while i<N:
		if v > S[i]/(1-K[i]/(D*1.0)):
			v=S[i]/(1-K[i]/(D*1.0))
		i=i+1
	q=a+1
	r="Case #"+str(q)+": "+str(v)
	print r
	a=a+1
	



 