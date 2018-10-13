#x=input("")
f=open("A-large.in")
T=f.readline()
count=0
for lines in f:
	count+=1
	lines=lines.strip()
	qqww=lines.split(" ")
	if len(qqww)==2:
		d=list(qqww[1])
		d=list(map(int, d))
		sp=[]
		s=d[0]
		c=0;summ=0;
		for i in range(1,len(d)):
			if d[i]==0:
				pass
			elif i <= s:
				s=s+d[i]
			elif i > s:
				c=i-s
				summ=summ+c
				s=s+d[i]+c
		print("Case #"+str(count)+": "+str(summ))
	else:
		print("Case #"+str(count)+": 0")
