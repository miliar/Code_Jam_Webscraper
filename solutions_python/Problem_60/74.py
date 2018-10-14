
C = int(raw_input())
for nocase in range(1, C+1):
	result = 0
	N, K, B, T = tuple(map(int, raw_input().split()))
	xs = map(int, raw_input().split())
	vs = map(int, raw_input().split())
	xs_vs = zip(xs, vs)

	xs_vs.sort()
	time_chicks = []
	for x, v in xs_vs:
		time_chicks.append(float(B - x) / v)
	time_chicks.reverse()
	
	nb_ok = 0
	nb_bad = 0
	for t in time_chicks:
		if nb_ok == K:
			break
		
		if t <= T:
			result += nb_bad
			nb_ok += 1
		else:
			nb_bad += 1
	
	if nb_ok != K:
		print 'Case #%d: IMPOSSIBLE' % nocase
	else:
		print 'Case #%d: %d' % (nocase, result)
	