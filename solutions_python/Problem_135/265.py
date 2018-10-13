fin = open('A-small.in', 'r')
fout = open('A.out', 'w')

t = int(fin.readline())
for i in xrange(t):
	r1 = int(fin.readline())
	for r in xrange(4):
		line = fin.readline()
		if r + 1 == r1:
			s1 = set(line.split())
	r2 = int(fin.readline())
	for r in xrange(4):
		line = fin.readline()
		if r + 1 == r2:
			s2 = set(line.split())
	fout.write('Case #%d: ' % (i + 1))
	if len(s1 & s2) == 0:
		fout.write('Volunteer cheated!\n')
	elif len(s1 & s2) > 1:
		fout.write('Bad magician!\n')
	else:
		fout.write('%s\n' % list(s1 & s2)[0])
