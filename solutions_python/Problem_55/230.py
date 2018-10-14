#/usr/bin/python3

t = int(input())
for c in range(t):
	r, k, n = map(int, input().strip().split())
	queue = list(map(int, input().strip().split()))
	coaster = []
	m = 0
	for cr in range(r):
		s = 0
		while queue and s + queue[0] <= k:
			g = queue.pop(0)
			coaster.append(g)
			s += g
		while coaster:
			queue.append(coaster.pop(0))
		m += s
	print('Case #%d: %d' % (c+1, m))
