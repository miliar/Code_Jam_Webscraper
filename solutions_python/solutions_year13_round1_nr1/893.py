import math
a=input()
k=1
while(a):
	b=raw_input()
	b=b.split()
	r=int(b[0])
	t=int(b[1])
	n=(2.0*r-1.0)*(2.0*r-1.0)
	n=n+8.0*t
	n=math.sqrt(n)
	n=(n+(1.0-2.0*r))/4.0
	n=int(n)
	print "Case #"+`k`+":",
	print n
	a=a-1
	k=k+1
