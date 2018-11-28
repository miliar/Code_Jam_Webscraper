t=input()
case=1
while t!=0:
	a=raw_input().split()
	c=float(a[0])
	f=float(a[1])
	x=float(a[2])
	s=2.0
	ans=0.0
	while True:
		a1=x/s
		b=c/s
		c1=x/(s+f)
		if(b+c1 < a1):
			s+=f
			ans+=b
		else:
			ans+=x/s
			break
	print "Case #%d"%case+": %.7f"%ans
	case+=1
	t-=1
