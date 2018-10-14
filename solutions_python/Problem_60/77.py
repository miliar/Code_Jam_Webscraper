def solve(tc):
	n,k,b,t = map(int, raw_input().split())
	x = map(int, raw_input().split())
	v = map(int, raw_input().split())
	assert(len(x) == n and len(v) == n)
	chicks = sorted(zip(x,v))
	chicks.reverse()

	done = 0
	swaps = 0
	bad = 0
	
	for c in chicks:
		if done >= k:
			break
			
		x, v = c[0], c[1]
		eta = float(b - x)/v
	
		if eta > t:
			bad+=1
		else:
			swaps += bad
			done += 1
		
	print "Case #%d:"%tc,
	if done < k:	
		print "IMPOSSIBLE"
	else:
		print swaps

for tc in xrange(input()):
	solve(tc+1)