import math

f=open('C-large-1.in','r')
fout=open('C-large-1.out','w')
T=int(f.readline())
num=10**7

d=[0]*(num+1)
cc=0
for i in xrange(1,num+1):
	g=str(i)
	if g==g[::-1]:
		gsq=str(i*i)
		if gsq==gsq[::-1]:
			cc+=1
	d[i]=cc

for t in xrange(1,T+1):
	sB,eB=f.readline().split()
	s=int(math.ceil(math.sqrt(int(sB))))
	e=int(math.sqrt(int(eB)))
	c=d[e]-d[s-1]
	
	fout.write('Case #'+str(t)+': '+str(c)+'\n')		
f.close()
fout.close()
