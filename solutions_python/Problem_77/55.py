from math import *

filename = 'D-large'
fin = open('%s.in' % filename)
fout = open('%s.out' % filename, 'w')

cases = int(fin.readline().strip())
for case in xrange(cases):
	n = int(fin.readline().strip())
	a = [int(x) for x in fin.readline().strip().split()]
	s = 0
	for i in xrange(n):
		if (a[i] != (i+1)): s += 1
	fout.write('Case #%d: %d.000000\n' % (case+1, s))

fin.close()
fout.close()
