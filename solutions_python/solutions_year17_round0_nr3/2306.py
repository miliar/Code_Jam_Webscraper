from math import floor, ceil, log

T = int(raw_input().strip())
for t in range(1, T+1):
	N, K = map(int, raw_input().strip().split())
	counts = {}
	current_gap = N
	counts[N] = 1
	for i in range(K):
		counts[current_gap] -= 1		
		upper = int(floor(current_gap/2))
		if current_gap % 2 == 0:
			lower = int(floor(current_gap/2)) - 1
		else:
			lower = upper
		if upper in counts.keys():
			counts[upper] += 1
		else:
			counts[upper] = 1

		if lower in counts.keys():
			counts[lower] += 1
		else:
			counts[lower] = 1

		if counts[current_gap] == 0:
			counts.pop(current_gap, None)
			current_gap = max(counts.keys())	
	print 'Case #{0}: {1} {2}'.format(t, upper, lower)


