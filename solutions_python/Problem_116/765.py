n = 0
i = 0
cases = []

with open('A-large.in') as f:
	n = int(f.readline().strip())
	cases = [[] for j in xrange(n)]
	for entry in f:
		entry = entry.strip()
		if len(entry) == 0:
			i += 1
		else:
			chars = list(entry)
			cases[i].append(chars)

def process_case(case):
	xs_in_d = [0, 0]
	ys_in_d = [0, 0]

	xs_in_r = [0 for i in xrange(4)]
	ys_in_r = [0 for i in xrange(4)]
	
	xs_in_c = [0 for i in xrange(4)]
	ys_in_c = [0 for i in xrange(4)]
	
	completed = True
	for r in xrange(4):
		for c in xrange(4):
			if case[r][c] == '.':
				completed = False
			elif case[r][c] == 'X':
				xs_in_r[r] += 1
				xs_in_c[c] += 1
				if r == c:
					xs_in_d[0] += 1
				if r + c == 3:
					xs_in_d[1] += 1
			elif case[r][c] == 'O':
				ys_in_r[r] += 1
				ys_in_c[c] += 1
				if r == c:
					ys_in_d[0] += 1
				if r + c == 3:
					ys_in_d[1] += 1
			elif case[r][c] == 'T':
				xs_in_r[r] += 1
				xs_in_c[c] += 1
				ys_in_r[r] += 1
				ys_in_c[c] += 1
				if r == c:
					xs_in_d[0] += 1
					ys_in_d[0] += 1
				if r + c == 3:
					xs_in_d[1] += 1
					ys_in_d[1] += 1
			if xs_in_r[r] == 4 or xs_in_c[c] == 4 or 4 in (xs_in_d):
				return 'X won'
			if ys_in_r[r] == 4 or ys_in_c[c] == 4 or 4 in (ys_in_d):
				return 'O won'

	if (completed): return 'Draw'

	#print '--'
	#for row in case:
	#	print row
	#print '--'

	#print 'xs_in_r', xs_in_r
	#print 'ys_in_r', ys_in_r
	#print 'xs_in_c', xs_in_c
	#print 'ys_in_c', ys_in_c
	#print 'xs_in_d', xs_in_d
	#print 'ys_in_d', ys_in_d

	return 'Game has not completed'

i = 0
for case in cases:
	print 'Case #{0}: {1}'.format(i + 1, process_case(case))
	i += 1