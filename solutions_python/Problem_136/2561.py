t=int(raw_input())
for i in range(t):
	l=[float(x) for x in raw_input().split()]
	c=l[0]
	f=l[1]
	x=l[2]
	init=2
	totalcost=0.0
	comp1=c/init + x/(init + f)
	comp2= x/init 
	while(comp2>comp1):
		totalcost=totalcost+c/init
		init=init+f
		comp1=c/init + x/(init + f)
		comp2= x/init
	totalcost=totalcost+comp2
	print "Case #%d: %f" % (i+1, totalcost)

