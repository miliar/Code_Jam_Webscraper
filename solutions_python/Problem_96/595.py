import sys

count = int(sys.stdin.readline())
for i in xrange(0, count):
	tc = i+1
	strin = sys.stdin.readline()[:-1]
	values = strin.split ( ' ' )
	N = int(values[0])
	S = int(values[1])
	p = int(values[2])
	ts = values[3:]
	#print N, S, p
	#print t
	
	res = 0
	
	for i in range(0,N):
		t = int(ts[i])
		val = t/3
		rem = t%3
		
		if rem <> 0:
			val = val+1
		
		#print t, val, rem
		if val >= p:
			res = res + 1
			#print "%d >= %d" % ( val, p )
		elif rem <> 1 and t > 1 and S > 0 and val+1>=p:
			res = res + 1
			S = S - 1
			#print "special"
	
	print "Case #%d: %d" % ( tc, res )