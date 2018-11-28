#!/usr/bin/python

t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
	n = [int(_) for _ in raw_input()]
	for i in range(len(n)-1, 0, -1):
		if n[i] < n[i-1]:
			n[i] = 9
			for j in range(i + 1, len(n)):
				n[j] = 9
			n[i-1] = (n[i-1] + 9) % 10
	if n[0] == 0:
		n = n[1:]
	print 'Case', ('#%d:' % case), ''.join([str(_) for _ in n])
	
