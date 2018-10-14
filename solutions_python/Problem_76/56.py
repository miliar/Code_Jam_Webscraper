from math import *

filename = 'C-large'
fin = open('%s.in' % filename)
fout = open('%s.out' % filename, 'w')

cases = int(fin.readline().strip())
for case in xrange(cases):
	n = int(fin.readline().strip())
	c = [int(x) for x in fin.readline().strip().split()]
	s = 0
	sum = 0
	m = 10000000
	for i in xrange(n):
		s ^= c[i]
		sum += c[i]
		m = min(m, c[i])
	if (s != 0):
		fout.write('Case #%d: %s\n' % (case+1, 'NO'))
	else:
		fout.write('Case #%d: %d\n' % (case+1, sum - m))

fin.close()
fout.close()
