

with open('input') as f:
	lines = f.read().split('\n')

items = int(lines[0])
c = 1

for x in xrange(items):
	row1 = int(lines[c])
	row2 = int(lines[c+5])
	s1 = set(lines[row1+c].split(' '))
	s2 = set(lines[row2+c+5].split(' '))
	r = s1.intersection(s2)
	if len(r) == 1:
		print 'Case #{0}: {1}'.format(x+1, r.pop())
	elif len(r) > 1:
		print 'Case #{0}: Bad magician!'.format(x+1)
	elif len(r) < 1:
		print 'Case #{0}: Volunteer cheated!'.format(x+1)
	c += 10
