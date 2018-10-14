CB = [0,0,
		[(1,1)],
		[(1,2),(1,1,1),(2,2,2)],
		[(1,3),(2,2),(1,1,2),(2,3,3),(1,1,1,1),(3,3,3,3)]]

TC = int(input())
for tc in range(TC):
	N, P = map(int, input().split())
	G = list(map(int, input().split()))
	res = []
	byg = [0]*P
	for g in G:
		byg[g%P] += 1
	while byg[0] > 0:
		res.append(0)
		byg[0] -= 1
	for cb in CB[P]:
		rqs = [0]*P
		for x in cb:
			rqs[x] += 1
		while True:
			works = True
			for i in range(P):
				if rqs[i] > byg[i]:
					works = False
			if not works:
				break
			for x in cb:
				byg[x] -= 1
				res.append(x)
	for i in range(P):
		for a in  range(byg[i]):
			res.append(i)
	ans = 0
	cur = 0
	for a in res:
		if cur == 0:
			ans += 1
		cur = (cur + a) % P
	print("Case #%d: %d" % (tc+1, ans))
