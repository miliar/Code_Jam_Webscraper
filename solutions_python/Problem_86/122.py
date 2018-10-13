
T = int(raw_input())

for t in range(1, T+1):
	N, L, H = tuple(map(int, raw_input().split()))
	freqs = map(int, raw_input().split())
	ret = None
	
	for i in range(L, H+1):
		ok = True
		for f in freqs:
			if f % i != 0 and i % f != 0:
				ret = i
				ok = False
				break
		if ok:
			break
	
	if ok:
		print 'Case #%d: %d' % (t, i)
	else:
		print 'Case #%d: NO' % t
		
