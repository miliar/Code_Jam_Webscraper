f1=open("A.in","r")
f2=open("A.out","w")
a=list(map(lambda x:x.split(),f1.readlines()[1:]))
q=list(map(lambda x:str(x[1]),a))
l={}
p={}
y={}
c={}
for i in range (1,len(q)+1):
	l[i]=q[i-1]
	c[i]=[]
	for digit in l[i]:
		c[i].append(int(digit))

	p[i]=c[i][0]
	y[i]=0
	for k in range (1,(len(c[i]))):
		if p[i]<k:
			if c[i][k]!=0:
				y[i]+=(k-p[i])
				p[i]+=y[i]
		p[i]=p[i]+c[i][k]
m=''
for i in range(1,len(q)+1):
	m=m+'Case'+' '+'#'+str(i)+':'+' '+str(y[i])+'\n'
f2.write(m)
f1.close()
f2.close()

