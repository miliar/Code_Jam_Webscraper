#!/usr/bin/env python

# -2 -2 X   # +4
# -2 -1 X   # +3
# -2  0 X
#  2  0 X
#  2  1 X
#  2  2 X

# -1 -1 X   # +2
# -1  0 X   # +1
#  0  0 X   #  0
#  1  0 X   # -
#  1  1 X   # -

import re


def cnt(g, s, nr):
	"""
		g - googlers points,
		s - amount of surprises,
		nr - min number
	"""
	normal = 0
	may_be = 0

	xn = max((nr - 1) * 3 + 1, nr)
	xs = max((nr - 2) * 3 + 2, nr)

	for i in g:
		if i >= xn:
			normal = normal + 1
		elif i >= xs:
			may_be = may_be + 1

	if s > may_be:
		s = may_be
	return normal + s


N = input()

for i in range(N):
	line = [int(x) for x in re.split(' +', raw_input().strip())]
	s = line[1]
	nr = line[2]
	print "Case #%d: %d" % (i + 1, cnt(line[3:], s, nr))
