t = int(raw_input())
for i in xrange(1, t + 1):
	d, n = [int(s) for s in raw_input().split(" ")]
	maxtime = 0
	curtime = 0
	for j in xrange(n):
		start, maxspeed = ([float(s) for s in raw_input().split(" ")])
		curtime = (d-start)/maxspeed
		if (curtime > maxtime):
			maxtime = curtime
	speed = d/maxtime
	print "Case #{0[0]:d}: {0[1]:.6f}".format([i, speed])