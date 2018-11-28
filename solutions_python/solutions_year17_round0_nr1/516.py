from collections import deque

T = int(raw_input())

for qw in range(1, T+1):
		a, b = raw_input().split()
		cakes = [x == '+' for x in a]
		k = int(b)
		flips = 0
		for i in range(len(cakes) - k + 1):
			if not cakes[i]:
				flips = flips + 1
				for j in range(i, i + k) :
					cakes[j] = not cakes[j]
		print 'Case #%d:' % qw,
		if cakes == [True] * len(cakes):
			print flips
		else:
			print 'IMPOSSIBLE'
