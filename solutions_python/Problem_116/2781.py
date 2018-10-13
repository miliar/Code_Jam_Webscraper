lines = filter(None, [line.rstrip('\n') for line in open('A-small-attempt2.in')])

casen = int(lines[0])
cases = (lines[i:i+4] for i in xrange(1, len(lines[1:]), 4))

def won(b, l):
	# h1, h2, h3, h4, v1, v2, v3, v4, dl, dr
	return ((b[0][0] == l or b[0][0] == 'T')	and	(b[0][1] == l or b[0][1] == 'T')	and (b[0][2] == l or b[0][2] == 'T')	and (b[0][3] == l or b[0][3] == 'T')) or \
		   ((b[1][0] == l or b[1][0] == 'T')	and	(b[1][1] == l or b[1][1] == 'T')	and (b[1][2] == l or b[1][2] == 'T')	and (b[1][3] == l or b[1][3] == 'T')) or \
		   ((b[2][0] == l or b[2][0] == 'T')	and (b[2][1] == l or b[2][1] == 'T')	and (b[2][2] == l or b[2][2] == 'T')	and (b[2][3] == l or b[2][3] == 'T')) or \
		   ((b[3][0] == l or b[3][0] == 'T')	and (b[3][1] == l or b[3][1] == 'T')	and (b[3][2] == l or b[3][2] == 'T')	and (b[3][3] == l or b[3][3] == 'T')) or \
		   ((b[0][0] == l or b[0][0] == 'T')	and (b[1][0] == l or b[1][0] == 'T')	and (b[2][0] == l or b[2][0] == 'T')	and (b[3][0] == l or b[3][0] == 'T')) or \
		   ((b[0][1] == l or b[0][1] == 'T')	and (b[1][1] == l or b[1][1] == 'T')	and (b[2][1] == l or b[2][1] == 'T')	and (b[3][1] == l or b[3][1] == 'T')) or \
		   ((b[0][2] == l or b[0][2] == 'T')	and (b[1][2] == l or b[1][2] == 'T')	and (b[2][2] == l or b[2][2] == 'T')	and (b[3][2] == l or b[3][2] == 'T')) or \
		   ((b[0][3] == l or b[0][3] == 'T')	and (b[1][3] == l or b[1][3] == 'T')	and (b[2][3] == l or b[2][3] == 'T')	and (b[3][3] == l or b[3][3] == 'T')) or \
		   ((b[0][0] == l or b[0][0] == 'T')	and	(b[1][1] == l or b[1][1] == 'T')	and (b[2][2] == l or b[2][2] == 'T')	and (b[3][3] == l or b[3][3] == 'T')) or \
		   ((b[0][3] == l or b[0][3] == 'T')	and (b[1][2] == l or b[1][2] == 'T')	and (b[2][1] == l or b[2][1] == 'T')	and (b[3][0] == l or b[3][0] == 'T'))

def in_progress(b):
	for i in b:
		if '.' in i:
			return True
		return False

def check(case):
	if won(case, 'X'):
		return 'X won'
	elif won(case, 'O'):
		return 'O won'
	else:
		if in_progress(case):
			return 'Game has not completed'
		else:
			return 'Draw'

for x, y in enumerate(cases):
	print "Case #%d: %s" % (x + 1, check(y))
