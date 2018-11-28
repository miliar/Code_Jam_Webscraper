for cc in xrange(1, input() + 1):
	n, m = map(int, raw_input().split())
	A = []
	for _ in xrange(n):
		A.append(raw_input()[:m])
	pos = True
	ans = 0
	for i in xrange(n):
		for j in xrange(m):
			if A[i][j] != ".":
				u, d, l, r = False, False, False, False
				for k in xrange(i + 1, n):
					if A[k][j] != ".":
						d = True
						break
				for k in xrange(i):
					if A[k][j] != ".":
						u = True
						break
				for k in xrange(j + 1, m):
					if A[i][k] != ".":
						r = True
						break
				for k in xrange(j):
					if A[i][k] != ".":
						l = True
						break
				if not (u or d or l or r):
					pos = False
					break
				ans += 1
				if A[i][j] == ">" and r:
					ans -= 1
				if A[i][j] == "^" and u:
					ans -= 1
				if A[i][j] == "<" and l:
					ans -= 1
				if A[i][j] == "v" and d:
					ans -= 1
		if not pos:
			break
	if pos:
		print "Case #" + str(cc) + ": " + str(ans)
	else:
		print "Case #" + str(cc) + ": IMPOSSIBLE"
