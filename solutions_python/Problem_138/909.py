import sys
fopen=open('/Users/subodhyadav/Desktop/D-large.in.txt','r')
fout=open('/Users/subodhyadav/Desktop/D-large.out.txt','a')
for e in xrange(int(fopen.readline().strip())):
	x=int(fopen.readline().strip())
	l=map(float,fopen.readline().strip().split())
	m=map(float,fopen.readline().strip().split())
	p=sorted(l,reverse=True)
	q=sorted(m,reverse=True)
	n,k,j,i=0,0,-1,-1
	while True:
		i+=1
		if i>=x:
			break
		temp=p[i]
		while True:
			j+=1
			if j>=x:
				break
			if temp>q[j]:
				n+=1
				break
	j,i=-1,-1
	while True:
		i+=1
		if i>=x:
			break
		temp=q[i]
		while True:
			j+=1
			if j>=x:
				break
			if temp>p[j]:
				k+=1
				break
	s=x-k	
	fout.write("Case #")
	fout.write(str(e+1))
	fout.write(": ")
	fout.write(str(n))
	fout.write(" ")
	fout.write(str(s))
	fout.write("\n")
fout.close()
fopen.close()