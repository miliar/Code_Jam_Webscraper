# encoding: utf-8

import sys

def st_value(name, n, lo):
	i   = lo
	L   = len(name)
	cnt = 0
	while i < L:
		if name[i] not in ['a', 'e', 'i', 'o', 'u']:
			cnt = cnt + 1
			if cnt == n:
				return i
		else:
			cnt = 0
		
		i = i + 1
	
	return L

def n_value(name, n):
	r = []
	lo = 0
	L = len(name)
	while lo < L:
		hi = st_value(name, n, lo)
		if hi >= L:
			break
		r.append((lo, hi))
		lo = lo + 1
	# print r
	s = 0
	for (x, y) in r:
		s = s + L - y
	
	return s
	
	
	
	
	

if __name__ == '__main__':
	T = int(sys.stdin.readline())
	for i in xrange(1, T+1):
		line = sys.stdin.readline().rstrip().split()
		# print line[0], line[1]
		name = line[0]
		n    = int(line[1])
		nval = n_value(name, n)
		print 'Case #%d: %d' % (i, nval)