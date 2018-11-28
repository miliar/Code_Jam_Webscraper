file=open("A-large.in",'r')
t=int(file.readline())
out=open("out3.txt",'w')
for i in range(1,t+1):
	[d,n]=file.readline().split()
	[d,n]=[float(d),int(n)]
	[k1,s1]=file.readline().split()
	[k1,s1]=[float(k1),float(s1)]
	for j in range(n-1):
		[k,s]=file.readline().split()
		[k,s]=[float(k),float(s)]
		if ((d-k1)/s1)<((d-k)/s):
			k1=k
			s1=s
	ans=float(d*s1/(d-k1))		
	out.write('Case #%d: %f\n'%(i,ans))	
file.close()
out.close() 		
