f=open("teste","r")
pika=f.read()
pika=pika.split()
T=int(pika.pop(0))
o=0
while T!=0:
	o=o+1
	k=0
	T=T-1
	n=int(pika.pop(0))
	s=int(pika.pop(0))
	p=int(pika.pop(0))
	i=0
	g=[]
	while i<n:
		g=g+[int(pika.pop(0))]
		i=i+1
	i=0
	a=p
	b=p-2
	c=p-2
	while i<len(g):
		if g[i]-a<0:
			u=0
		elif g[i]-3*p+2>=0:
			k=k+1
		elif s>0 and g[i]-3*p+4>=0:
			k=k+1
			s=s-1
		i=i+1
	print k
	q=open("respgoo.txt","a")
        q.write("Case #"+str(o)+": "+str(k)+"\n")

