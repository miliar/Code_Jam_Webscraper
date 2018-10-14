from heapq import heappop, heappush

T = int(input())
for x in range(1, T + 1):
	N, K = map(int, input().split())
	ds = [(N, 1)]
	ddict = {N: 1}
	h = [-N]
	while K > 0:
		d = - heappop(h)
		c = ddict.pop(d)
		K -= c
		z = (d-1) // 2
		y = (d-1) - z
		try:
			ddict[y] += c
		except KeyError:
			ddict[y] = c
			heappush(h, -y)
		try:
			ddict[z] += c
		except KeyError:
			ddict[z] = c
			heappush(h, -z)
	print('Case #%d: %d %d' % (x, y, z))
