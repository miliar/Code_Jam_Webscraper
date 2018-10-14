file = "A-large.in.txt"

data = [ l.strip().split()  for l in open(file).read().split('\n') ]

lines = int(data[0][0])



for i in xrange(lines):
	N = int( data[i+1][0] ) 
	K = int( data[i+1][1] ) 
	
	x = [(K >> y) & 1 for y in range(N-1, -1, -1)]
	
	if sum(x) == len(x):
		print "Case #%d: ON" % (i+1)
	else:
		print "Case #%d: OFF" % (i+1)
	