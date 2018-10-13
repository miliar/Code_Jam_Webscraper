import sys

if __name__ == "__main__":
	infile = sys.stdin
	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		if fn != '-':
			infile = open(fn)

	t = int(infile.readline())
	for _t in xrange(t):
		row = infile.readline().strip().split(' ')
		c = float(row[0])
		f = float(row[1])
		x = float(row[2])

		lastvalue = float("inf")
		emptyrate = 2.0
		farms = 0
		timetofarm = 0.0

		while True:
			rate = emptyrate + farms * f
			if c / rate > x / rate:
				lastvalue = x / rate + timetofarm
				break
			totaltime = timetofarm + x / rate
			timetofarm = timetofarm + (c / rate)
			if lastvalue < totaltime:
				break
			lastvalue = totaltime
			farms = farms + 1

		print "Case #%d: %f" % (_t + 1, lastvalue)