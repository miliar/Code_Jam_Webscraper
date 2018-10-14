#!/usr/bin/env python

f = open('C-small-1-attempt0.in', 'r')
w = open('C-small-1-attempt0.out', 'w')

n = int(f.readline())
for i in range(0, n):
	s, p = map(int, f.readline().split(' '))

	a = [False] * (s + 2)
	a[0] = True
	a[s + 1] = True

	xmin = -1
	xmax = -1

	for c in range(0, p):		
		l = 0
		cg = 0
		mg = 0
		x = -1

		for j in range(1, s + 2):
			if a[j]:
				m = l + (j - l) / 2
				
				if m < 0:
					m = 0
				ml = m - l - 1
				mr = j - m - 1

				if cg > mg:					
					mg = cg
					x = m
					if ml > mr:
						xmin = mr
						xmax = ml
					else:
						xmin = ml
						xmax = mr

				cg = -1
				l = j

			cg += 1

		a[x] = True

	w.write('Case #%i: %i %i\n' % (i + 1, xmax, xmin))

f.close()
w.close()