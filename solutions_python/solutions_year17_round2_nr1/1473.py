hour = 0
t = int(raw_input())
for i in xrange(1, t + 1):
	d, n = [int(s) for s in raw_input().split(" ")]
	for j in xrange(0, n):
		k, s = [int(s) for s in raw_input().split(" ")]
		otherHour = float(d - k) / s
		if(otherHour > hour):
			hour = otherHour
	print "Case #{}: {}".format(i, d/hour)
	hour = 0