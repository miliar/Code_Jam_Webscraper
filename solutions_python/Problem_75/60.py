from math import *

filename = 'B-large'
fin = open('%s.in' % filename)
fout = open('%s.out' % filename, 'w')

cases = int(fin.readline().strip())
for case in xrange(cases):
	line = fin.readline().strip().split()
	combination = dict()
	opposition = dict()
	p = 0
	c = int(line[p])
	for i in xrange(c):
		p += 1
		s = line[p]
		combination[(s[0],s[1])] = s[2]
		combination[(s[1],s[0])] = s[2]
	p += 1
	d = int(line[p])
	for i in xrange(d):
		p += 1
		s = line[p]
		opposition[(s[0],s[1])] = 0
		opposition[(s[1],s[0])] = 0
	p += 1
	n = int(line[p])
	p += 1
	spell = line[p]
	s = []
	for i in xrange(n):
		s.append(spell[i])
		l = len(s)
		if (l > 1 and (s[l-1],s[l-2]) in combination):
			t = combination[(s[l-1],s[l-2])]
			del s[l-2:l]
			s.append(t)
			continue
		for j in xrange(l-1):
			if ((s[j],s[l-1]) in opposition):
				s = []
				break
	s = str(s).replace('\'','')
	fout.write('Case #%d: %s\n' % (case+1, s))

fin.close()
fout.close()
