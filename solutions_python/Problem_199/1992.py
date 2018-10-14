#!/usr/bin/env python

f = open('A-large.in', 'r')
w = open('A-large.out', 'w')

n = int(f.readline())
for i in range(0, n):
	r = 'IMPOSSIBLE'

	l = f.readline()
	pl, fli = l.split(' ')
	p = list(pl)
	fl = int(fli)

	t = 0
	s = False
	j = 0

	for j in range(0, len(p)):
		if (j + fl - 1) < len(p):
			if p[j] == '-':
				p[j] = '+'

				for k in range(j, j + fl):
					if p[k] == '+':
						p[k] = '-'
					else:
						p[k] = '+'

				t += 1
		else:
			ss = True
			for k in range(j, j + fl - 1):
				if p[k] == '-':
					ss = False

			s = ss
			break

	if s:
		r = t

	w.write('Case #%i: %s\n' % (i + 1, r))

f.close()
w.close()