for i in xrange(1, int(raw_input()) + 1):
	C, F, X = [float(token) for token in raw_input().split()]
	R = 2.0
	K = 0.0
	time = 0.0
	while(X > K):
		if K >= C:
			if(((X - K)/R) > ((X - (K -C))/(R + F))):
				#print "#1"
				K = K - C
				R = R + F
			else:
				#print "#2"
				K = X
				time = time + ((X - K)/R)
		else:
			if(((X - K)/R) > ((X/(R+F)) + ((C-K)/R))):
				#print "#3"
				time = time + ((C-K)/R)
				R = R + F
				K = 0
			else:
				#print "#4"
				time = time + ((X - K)/R)
				K = X
	print "Case #%d: %.7f" % (i, time)

