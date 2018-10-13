nc = input()

for ii in xrange(1,nc+1):
	D,n = map(int, raw_input().split(" "))
	D = float(D)
	slowest = -999999999999999999999999999
	for i in xrange(n):
		pos, speed = map(int, raw_input().split(" "))
		pos = float(pos)
		speed = float(speed)
		c = (D - pos)/speed
		if c > slowest:
			slowest = c
	print "Case #%d: %f"%(ii, D/slowest)
