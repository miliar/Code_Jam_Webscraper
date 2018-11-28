def parse_row(row):
	return set(map(int, row.split()))

tests = int(raw_input())

for test in xrange(1, 1+tests):
	row1 = int(raw_input())
	for i in xrange(1, 5):
		row = raw_input()
		if i == row1:
			grid1 = parse_row(row)
	row2 = int(raw_input())
	for i in xrange(1, 5):
		row = raw_input()
		if i == row2:
			grid2 = parse_row(row)
	both = grid1&grid2
	if not both:
		answer = 'Volunteer cheated!'
	elif len(both) > 1:
		answer = 'Bad magician!'
	else:
		answer = next(iter(both))
	print 'Case #%s: %s' % (test, answer)
