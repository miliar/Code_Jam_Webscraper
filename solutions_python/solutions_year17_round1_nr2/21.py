def bound(qss, ps):
	ret = 0
	for i, j in enumerate(ps):
		if j >= P:
			return -1
		ret = max(ret, qss[i][j][0])
	return ret


for x in range(1, int(input()) + 1):
	N, P = map(int, input().split())
	Rs = list(map(int, input().split()))
	Qss = []
	for i, n in enumerate(range(N)):
		r = Rs[i]
		row = []
		for cell in map(int, input().split()):
			row.append((((cell * 10) + (r * 11 - 1)) // (r * 11), (cell * 10) // (r * 9)))
		row.sort()
		Qss.append(row)
	ps = [0] * N
	ans = 0

	while True:
		l = bound(Qss, ps)
		if l == -1:
			break
		failed = False
		for i, j in enumerate(ps):
			if Qss[i][j][1] < l:
				ps[i] += 1
				failed = True

		if not failed:
			ans += 1
			ps = [x+1 for x in ps]

	print('Case #%d: %d' % (x, ans))
