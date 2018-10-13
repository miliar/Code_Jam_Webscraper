t = int(raw_input())

for i in xrange(t):
	D,N = map(int,raw_input().strip().split())

	mi=0
	for j in xrange(N):
		k,s = map(float,raw_input().strip().split())
		mi = max(mi,(D-k)/s)
	
	if mi==0:
	    print "Case #%d: %0.6f"%(i+1,10000)
	else:
	    print "Case #%d: %0.6f"%(i+1,float(D/mi))
        