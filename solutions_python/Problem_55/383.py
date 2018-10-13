fname="C-large"
inn=open(fname+".in")
out=open(fname+".out",'w')
for case in range(1,int(inn.readline())+1):
	r,k,n=map(int,inn.readline().rstrip().split())
	gs=map(int,inn.readline().rstrip().split())
	#a=[gs[0]]; for g in gs[1:]: a.append(a[-1]+g) #sumatoria
	a=[]
	for i in range(n):
		pos=(i+1)%n;s=gs[i]
		while s+gs[pos]<=k and pos!=i: s+=gs[pos]; pos+=1; pos%=n
		a.append((pos,s))
	#print a
	ciclo=[0]
	pos=a[0][0]
	while pos not in ciclo: ciclo.append(pos); pos=a[pos][0]
	#print ciclo
	ini=ciclo.index(pos)
	pre=ciclo[:ini]
	ciclo=ciclo[ini:]
	#print pre,ciclo
	res=0
	if r<ini:
		for i in xrange(r): res+=a[pre[i]][1]
	else:
		res+=sum([a[i][1] for i in pre])
		r-=len(pre)
		ciclosum=sum([a[i][1] for i in ciclo])
		res+=ciclosum*(r/len(ciclo))
		for i in xrange(r%len(ciclo)): res+=a[ciclo[i]][1]
		
	out.write("Case #%d: %d\n"%(case,res))
out.close()
#print open(fname+".out").read()
