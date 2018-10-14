t=input()
for tt in range(t) :
	c,f,x=map(float,raw_input().split())

	"""
	mt= x/2
	i=0
	while True:
		i+=1
		t=0
		for j in range(i):
			t+=c/(2+j*f)
		t+=x/(2+i*f)
		mt=min(mt,t)
		if mt<t :
			break
	"""

	mt=0
	i=0
	while True :
		if c/(2+i*f)+x/(2+i*f+f) < x/(2+i*f) :
			mt+=c/(2+i*f)
			i+=1
		else :
			mt+=x/(2+i*f)
			break
	

	print "Case #%d: %.7f"%((tt+1),mt)
	
	
#	mt=min(t0,t1,t2,...)
#	t0= x/2
#	t1= c/2 + x/(2+f)
#	t2= c/2 + c/(2+f) +x/(2+f+f)
#	t3= c/2 + c/(2+f) + c/(2+f+f) + x/(2+f+f+f)