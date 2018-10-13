filename = 'B-large'

with open(filename + '.in') as F, open(filename + '.out', 'w') as O:
	cases = int(F.readline())
	for case in xrange(cases):
		cfarm, ffarm, cgoal = (float(x) for x in F.readline().split())

		tpayback = cfarm/ffarm

		f = 2
		tfinal = cgoal/f
		tfarm = cfarm/f

		while tfarm < tfinal:
			f = f + ffarm
			if (tfarm + cgoal/f < tfinal):
				tfinal = tfarm + cgoal/f
			else:
				break
			tfarm = tfarm + cfarm/f

		O.write('Case #%d: %.7f\n' % (case + 1, tfinal))




