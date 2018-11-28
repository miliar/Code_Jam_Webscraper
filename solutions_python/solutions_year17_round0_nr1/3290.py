TT = int(raw_input())

def sol(cakes, cnt):
	res = 0
	while len(cakes) >= cnt:
		if all(cakes):
			return res
		cur = 0
		while cakes[cur]:
			cur += 1
		cakes = cakes[cur:]

		if len(cakes) < cnt:
			break

		cakes[0:cnt] = map(lambda x: not x, cakes[0:cnt])
		res += 1
	return float('inf')

for T in xrange(1, TT+1):
	cakes, cnt = raw_input().split(' ')
	def map_sign(s):
		return True if s=="+" else False

	res = sol(map(map_sign, cakes), int(cnt))
	print "Case #{}: {}".format(T, "IMPOSSIBLE" if res == float('inf') else res)
