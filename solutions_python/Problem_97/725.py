#!/usr/bin/env python

def main():
	import sys

	sys.stdin.readline()
	casenum = 1
	while True:
		line = sys.stdin.readline().strip()
		if line=='': break
		a, b = map( int, line.split(' ', 2) )
		
		count = 0
		
		for n in xrange(a, b+1):
			for permute in recycle(n):
				if inRange(permute, a, b) and permute != n:
					count += 1
					#print count, n, permute

		assert not count % 2
		print 'Case #%s:' % casenum, count / 2
		casenum += 1


def recycle(n):
	s = str(n)
	permutes = []
	# yield int(s)
	for i in xrange(len(s)-1):
		lastChar = s[-1]
		s = lastChar + s[:-1]
		if s in permutes: continue
		permutes.append(s)
		if lastChar=='0': continue
		yield int(s)

def inRange(n, a, b): return n >= a and n <= b

if __name__ == '__main__': main()
