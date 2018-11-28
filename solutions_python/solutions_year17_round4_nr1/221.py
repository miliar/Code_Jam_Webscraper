from sys import stdin
readline = stdin.readline

T = int(readline())
for t in xrange(1, T+1):
	N, P = map(int, readline().strip().split())
	G = map(int, readline().strip().split())
	
	if P == 2:
		evenCount = sum([1 if x%2 == 0 else 0 for x in G])
		oddCount = N - evenCount
		
		ans = evenCount + (oddCount+1)/2
	
	elif P == 3:
		zeromod = sum([1 if x%3 == 0 else 0 for x in G])
		onemod = sum([1 if x%3 == 1 else 0 for x in G])
		twomod = sum([1 if x%3 == 2 else 0 for x in G])
		
		ans = zeromod
		ans += min(onemod, twomod)
		tmp = max(onemod, twomod) - min(onemod, twomod)
		ans += tmp/3
		if tmp%3:
			ans += 1
	
	print 'Case #%d: %d' % (t, ans)
