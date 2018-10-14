#!/usr/bin/python
'''
Google codejam template
https://code.google.com/codejam/contest/1460488/dashboard#s=p2
'''
import sys
#fh = sys.stdin
fh = open(sys.argv[1])

cases = int(fh.readline())

for case in range(1, cases+1):
	print 'Case #%i:' % case,
	a, b = fh.readline().split()
	pairs = 0
	#print 'a=%s, b=%s' % (a, b)
	for intn in range(int(a), int(b)+1):
		mfound = {}
		n = str(intn)
		nn = 2 * n
		ln = len(n) # length of n
		assert a <= n, 'a=%s, n=%s' % (a, n)
		for i in range(1, ln):
			m = nn[i:i+ln]
			if n < m <= b:
				mfound[m] = 1
		pairs += len(mfound)
	print pairs
