#!/usr/bin/env python

import re
import sys

def calculate(audience):
	""" Given a string specifying the audience's
	characteristics, calculate the minimum number of
	additional audience members needed to ensure all
	audience members participate in a standing ovation.
	"""

    # short circuit when existing + additional >= max_shyness
	max_shyness = int(re.match('(\d+)', audience).group(1))
	audience = map(int, re.sub('^\d+ ', '', audience))

	# number of audience members in the specification
	existing   = 0

	# number of additional audience members needed to ensure
	# a standing ovation involving all audience members
	additional = 0

	# calculate the delta between shyness and the 
	# number of existing audience members, saving the
	# result to additional
	for (shyness, n) in enumerate(audience):
		if existing < shyness:
			delta = shyness - existing
			additional += delta
			existing   += delta
		existing += n
		if existing >= max_shyness:
			return additional
	else:
		return additional

if __name__ == '__main__':
	fn = sys.argv[1]
	casenum = 1
	with open(fn) as f:
		total_cases = f.readline().strip()
		for line in f:
			line = line.strip()
			print "Case #%d: %d" % (casenum, calculate(line))
			casenum += 1


