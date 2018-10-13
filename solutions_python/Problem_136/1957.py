from sys import argv
lines = open(argv[1]).readlines()
casecount = int(lines.pop(0))
for i in xrange(casecount):
	c, f, x = map(float, lines.pop(0).split())
	rate = 2.0
	cookies = 0
	seconds = 0.0
	while cookies < x:
		if (x-cookies)/rate > (c-cookies)/rate + x/(rate+f):
			seconds += (c-cookies)/rate
			rate += f
		else:
			seconds += (x-cookies)/rate
			break
	print "Case #%i: %f"%(i+1, seconds)