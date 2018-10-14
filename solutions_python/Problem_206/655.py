t = int(raw_input()) # this is the number of test cases
for i in xrange(1, t+1):
	d, n = str(raw_input()).split()
	d = int(d)
	n = int(n)

	slowest_time_rem = 0
	for horse in range(n):
		pos, speed = str(raw_input()).split()
		pos = int(pos)
		speed = int(speed)
		time_rem = (d - pos + 0.0) / speed
		if time_rem > slowest_time_rem:
			slowest_time_rem = time_rem

	result = '{:.6f}'.format(d / slowest_time_rem)

	print  "Case #{0}: {1}".format(i, result)