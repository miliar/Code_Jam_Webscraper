def getTimeToGoal(fc, fi, x):
	c = 0
	f = 0.0
	t = 0

	def i(f, fi):
		return 2.0 + f * fi

	t += fc / i(f, fi)
	c += i(f, fi) * t
	while (x - c + fc) / (i(f, fi) + fi) < (x - c) / i(f, fi):
		c -= fc
		f += 1

		delta = fc / i(f, fi) 
		t += delta 
		c += i(f, fi) * delta

	t += (x - c) / i(f, fi)
	return t 

input = open("B-large.in")
tests = int(input.readline())

for test in xrange(0, tests):
	data = [float(x) for x in input.readline().split(" ")]
	print "Case #%d: %.7f" % (test + 1, getTimeToGoal(*data))
