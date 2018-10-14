# coding: shift-jis

import sys

def Factor(N):
	ret = []
	d = 2
	d2= d**2
	while N >= d*2:
		if N % d == 0:
			ret += [d]
		d += 1
	return ret

def Iter(p, it):
	for i in it:
		if i % p == 0 or p % i == 0:
			yield i
	
	

f = file(sys.argv[1])

test_cnt = int(f.readline())

for case in range(1, test_cnt+1):
	N, L, H = map(int, f.readline().split())
	frs = map(int, f.readline().split())
	
	it = Iter(frs[0], xrange(L, H+1))
	for fr in frs[1:]:
		it = Iter(fr, it)
	
	try:
		val = it.next()
		ret = True
	except StopIteration:
		ret = False
	if ret:
		print 'Case #%d:'%case + ' %d'%val
	else:
		print 'Case #%d: NO'%case