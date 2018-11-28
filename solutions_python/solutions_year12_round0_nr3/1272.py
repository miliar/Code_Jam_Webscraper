#!/usr/bin/python

import time, sys, os, math
start = time.clock()
print os.path.dirname(sys.argv[0])
sys.stdout = open(os.path.dirname(sys.argv[0]) + r'\output.txt', 'w')

f = open(sys.argv[1], 'r')
T = int(f.readline())

for i in xrange(T):
	nums = map(int, f.readline().split())
	A, B = nums
	digits = int(math.floor(math.log10(A)))
	
	count = 0
	for n in xrange(A, B):
		m = n
		while 1:
			q, r = divmod(m, 10)
			m = int(r*10**digits) + q
			if m <= B and m > n:
				count += 1
			if m == n:
				break

	print 'Case #%d: %d' % (i + 1, count)