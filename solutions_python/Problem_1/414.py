def tr(se,qs):
	sw=-1
	h=range(len(se))
	while h[0]<>-1:
		for t in range(len(se)):
			if se[t] in qs:
				h[t]=qs.index(se[t])
			else:
				h[t]=-1
		h.sort()
		qs=qs[h[-1]:]
		sw+=1
	return sw

a=open("A-large.in","r")
b=a.readlines()
N=int(b[0])
c=1

for n in range(N):
	S=int(b[c])
	se=[]
	for i in range(S):
		se+=[b[c+i+1][:-1]]
	c+=S+1	

	Q=int(b[c])
	qs=[]
	for i in range(Q):
		qs+=[b[c+i+1][:-1]]
	c+=Q+1

	o=tr(se,qs)
	ou="Case #"+str(n+1)+": "+str(o)
	print ou
