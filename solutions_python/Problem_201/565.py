def left(o):
	z=o
	count=0
	while z>0:
		z=z/2
		count+=1
	count-=1
	if (o<3*2**(count-1)):#left
		return True
	return False


def fun(N,K):# if n is odd
	i=K
	r=N
	o=K
	x=[]
	m=0
	path=[]
	flag=0#right
	while i>0:
		x.append(i)	
		i=i/2
		m+=1
#	if (K<3*2**(m-1)):#left
#		flag=1
	
	#if flag:
#		o-=4
	m-=1
	while m>0:
	#	print m
		path.append(o)
		if left(o):
			o-=2**(m-1)
		else:
			o-=2**m
		m-=1
	z=[]	
	for q in range(len(path)-1,-1,-1):
		z.append(path[q])
#	print z
	for m in z:			
		if r%2==0:
			if left(m):
				r=r/2
			else:
				r=r/2-1
		else:
			r=r/2
	if r%2==0:
		a=r/2
		b=r/2-1
	else:
		a=r/2
		b=r/2
	as1=max(a,b)
	as2=min(a,b)
	as1=max(as1,0)
	as2=max(as2,0)
	return as1,as2
myout3=open("final92.txt","a")
with open('inp3.txt',"r") as f:
	inp=[]
	for line in f:
		inp.append(line)
inp=[x.strip() for x in inp]
t=int(inp[0])
#1 for filled
#0 for empty
for ind in range(1,t+1):
	N,K=map(int,inp[ind].split())
	#if 2*K==N:
	#	ma,mi=1,0
	#elif 2*K==N-2:
	#	ma,mi=1,0
	#else:
	ma,mi=fun(N,K)
	#print fun(N,K)
	myout3.write("Case #"+str(ind)+": "+str(ma)+" "+str(mi)+"\n")

