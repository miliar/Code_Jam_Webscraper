for t in range(int(input())):
	n, q = (int(i) for i in input().split())
	hs = [[int(i) for i in input().split()] for j in range(n)]
	ds = [[int(i) for i in input().split()][j + 1] for j in range(n - 1)]
	input()
	input()
	tc = [0] * n
	tc[n - 1] = 0
	for i in range(n - 2, -1, -1):
		min = -1
		sd = 0
		for j in range(1, n - i):
			sd += ds[i + j - 1]
			if sd > hs[i][0]:
				break
			if tc[i + j] == -1:
				continue
			tm = tc[i + j] + sd / hs[i][1]
			if min == -1 or tm < min:
				min = tm
		tc[i] = min
	print("Case #%d: %f" % (t + 1, tc[0]))