#!/usr/bin/env python2

def solve(a, b):
	count = 0

	for i in range(a, b):
		d = []
		for l in range(0, len(str(i))):
			front, back = str(i)[:l], str(i)[l:]
			if not back.startswith('0') and i < int(back + front) <= b:
				if (i, int(back + front)) not in d:
					count += 1
					d.append((i, int(back + front)))

	return count

with open('in.txt') as fin:
	with open('out.txt', 'w') as fout:
		T = int(fin.readline().strip())
		for case in xrange(T):
			A, B = [int(i) for i in fin.readline().strip().split()]
			print >>fout, 'Case #%d: %s' % (case+1, solve(A, B))
