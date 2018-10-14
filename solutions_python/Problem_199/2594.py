def fp(a,x):
	for i in range(0,x):
		p[0][a+i]=1-p[0][a+i]

f1=open("A-large.in","r")
f2=open("result.txt","w")
n=list(f1)
for i in range(1,int(n[0])+1):
	p=n[i].split()
	p[1]=int(p[1])
	p[0]=list(p[0])
	for j in range(0,len(p[0])):
		p[0][j]=int((45-ord(p[0][j]))/2)
	c=0
	d=0
	while 0 in p[0]:
		a=p[0].index(0)
		if a+p[1]>len(p[0]):
			d=1
			break
		else:
			fp(a,p[1])
			c+=1
	f2.write('Case #')
	f2.write(str(i))
	f2.write(': ')
	if d==0:
		f2.write(str(c))
		f2.write('\n')
	else:
		f2.write('IMPOSSIBLE\n')
