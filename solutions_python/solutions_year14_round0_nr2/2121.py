#-------------------------------------------------------------------------------

import sys

_lines = sys.stdin.readlines()
_pos   = 0

def read_line(offset, skip):
	global _pos
	line = _lines[_pos + offset]
	_pos += skip
	return line

def read_int(offset = 0, skip = 1):
	line = read_line(offset, skip)
	return int(line)

def read_intset(offset = 0, skip = 1):
	line = read_line(offset, skip)
	return {int(x) for x in line.split()}

def read_floatlist(offset = 0, skip = 1):
	line = read_line(offset, skip)
	return [float(x) for x in line.split()]

#-------------------------------------------------------------------------------

num_probs = read_int()

for index in xrange(num_probs):

	c, f, x = read_floatlist()

	delta_cookies = 2
	time = 0

	min_xtime = 10000000
	while True:
		delta_time = (x / delta_cookies)
		xtime = time + delta_time

		if min_xtime > xtime:
			min_xtime = xtime
		else:
			break

		delta_time = (c / delta_cookies)
		time += delta_time
		delta_cookies += f

	print "Case #%d: %.7f" % (index + 1, min_xtime)

