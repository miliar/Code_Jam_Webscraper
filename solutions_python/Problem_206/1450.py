for l in range(input()):
	print "Case #"+str(l+1)+":",
	d,n = map(float,raw_input().split())
	arr = []
	time=0
	for i in range(int(n)):
		q,w  = map(float,raw_input().split())
		time = max(time,(d-q)/w)
	fl = d/time
	print "%.6f" % fl
	