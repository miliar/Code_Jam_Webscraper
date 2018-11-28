import math
#f = open("B-sample.in")
f = open("/home/emre/Download/B-large.in")
g= open("output.txt","w")
numline=int( f.readline().strip("\n"))
for i in xrange(numline):
	print "%d out of %d" %(i+1, numline)
	num_bees = int( f.readline().strip("\n"))	
	xt, yt, zt, xvt, yvt, zvt = (0, )*6
	for bee in xrange(num_bees):
		(x, y, z, xv, yv, zv) = map(int, f.readline().strip("\n").split(" "))
		xt, yt, zt, xvt, yvt, zvt = xt+x, yt+y, zt+z, xvt+xv, yvt+yv, zvt+zv
	
	xt/=float(num_bees)
	yt/=float(num_bees)
	zt/=float(num_bees)
	xvt/=float(num_bees)
	yvt/=float(num_bees)
	zvt/=float(num_bees)
	
	try:
		t = (-1* (xt*xvt+yt*yvt+zt*zvt)) / (xvt**2 + yvt**2 + zvt**2)
	except ZeroDivisionError:
		t = 0
		
	if  t <=0:
		t = 0
	print "Minimum: ", t
	xlast = xt+xvt*t
	ylast = yt+yvt*t
	zlast = zt+zvt*t
	
	distance = math.sqrt(xlast*xlast + ylast*ylast + zlast*zlast)
	
	"""
	distance = math.sqrt(xt*xt + yt*yt + zt*zt)
	dmin=distance
	tmin = 0
	t = 0
	
	while True:
		t+=1
		xt+=xvt
		yt+=yvt
		zt+=zvt
		distance = xt*xt + yt*yt + zt*zt
		if distance > dmin:
			break
		else:
			dmin = distance
			tmin = t
	
	print "Minimum distance:",math.sqrt(dmin)
	print "Minimum time:",float(tmin)
	"""
	g.write("Case #%d: %f %0.8f\n" % (i+1 , distance, t))
g.close()
f.close()
