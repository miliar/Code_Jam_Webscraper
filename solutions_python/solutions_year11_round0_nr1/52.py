from math import *

filename = 'A-large'
fin = open('%s.in' % filename)
fout = open('%s.out' % filename, 'w')

cases = int(fin.readline().strip())
for case in xrange(cases):
	line = fin.readline().strip().split()
	pos = [1, 1]
	time = [0, 0]
	n = int(line[0])
	for i in xrange(n):
		c = line[1 + i * 2]
		if (c == 'O'):
			c = 0
		else:
			c = 1
		p = int(line[2 + i * 2])
		time[c] += abs(pos[c] - p) + 1
		time[c] = max(time[c], time[(c+1)%2]+1)
		pos[c] = p
	fout.write('Case #%d: %d\n' % (case+1, max(time[0], time[1])));

fin.close()
fout.close()
