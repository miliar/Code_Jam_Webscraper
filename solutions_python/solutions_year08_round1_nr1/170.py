import sys
import math


N = int(sys.stdin.readline())
for number in xrange(N):
	n = int(sys.stdin.readline())
	p = []
	q = []
	for i in sys.stdin.readline().split(' '):
		p.append (int(i))
	for i in sys.stdin.readline().split(' '):
		q.append (int(i))
	p.sort()
	q.sort(reverse=True)
	sum = 0
	for i in xrange(len(p)):
		sum += p[i]*q[i]

	print "Case #%d: %d" % (number+1, sum) 
					

