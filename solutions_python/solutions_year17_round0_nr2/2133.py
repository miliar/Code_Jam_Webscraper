#!/usr/bin/env python

f = open('B-large.in', 'r')
w = open('B-large.out', 'w')

n = int(f.readline())
for i in range(0, n):
	l = map(int, list(f.readline().strip()))

	h = -1
	hi = -1

	for j in range(0, len(l)):
		if l[j] > hi:
			hi = l[j]
			h = j

		if l[j] < hi:
			l[h] = hi - 1
			for k in range(h + 1, len(l)):
				l[k] = 9

	if l[0] == 0:
		l.pop(0)

	w.write('Case #%i: %s\n' % (i + 1, ''.join(map(str, l))))

f.close()
w.close()