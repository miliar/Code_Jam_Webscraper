fl=open('B-large.in','r')
p=open('ol','w+')
t=int(fl.readline())
ti=1
while ti<=t:
	xfc=fl.readline().split()
	c,f,x=(float(v) for v in xfc)
	n=0
	while True:
		b=2*c+c*n*f+f*c-x*f
		if b>0:
			break
		n+=1
	s=0
	for i in range(n):
		s+=1.0*c/(2+i*f)
	s+=1.0*x/(2+n*f)
	s= str("Case #")+str(ti)+str(": ")+str("%.7f" % s)+str(" \n")
	p.write(s)

	ti+=1