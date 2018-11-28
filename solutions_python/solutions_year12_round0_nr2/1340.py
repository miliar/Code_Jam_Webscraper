x=input()
for i in range(0,x):
	y=raw_input()
	z=y.split()
	n=z[0]
	s=z[1]
	p=z[2]
	l=[]
	for j in range(3,len(z)):
		l.append(z[j])
	l=[int(a) for a in l]
	l.sort()
#	print l
	no=len(l)
	maxp=3*int(p)-2
	count=0
	minp=3*int(p)-4
	p=int(p)
	if maxp<p:
		maxp=p
	if minp<p:
		minp=p
	k=no-1
	s=int(s)
#	print maxp,minp
#	print l
#	print s
	while k>=0 and l[k]>=maxp:
		count+=1
		k=k-1
	while k>=0 and l[k]>=minp and s>0:
		count+=1
		k=k-1
		s=s-1
	print "Case #"+str(i+1)+":",count
	
