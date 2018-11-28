def valid(ans):
	for x, y in zip(ans, ans[1:] + ans[0]):
		if x == y:
			return False
	return True

def anss(x, y):
	ans = ""
	ans2 = ""
	for i, j in zip(x, y):
		ans += i + j
		ans2 += j + i
	if len(x) > len(y):
		ans += x[N/2]
		ans2 += x[N/2]
	if len(x) < len(y):
		ans += y[N/2]
		ans2 += y[N/2]
	return ans, ans2

for t in xrange(1, input() + 1):
	N, R, RY, Y, YB, B, RB = map(int, raw_input().split())
	if max(R, Y, B) > N / 2:
		ans = "IMPOSSIBLE"
	else:
		ans = ""
		a = ["R"[:] * R + "Y"[:] * Y + "B"[:] * B, "Y"[:] * Y + "B"[:] * B + "R"[:] * R, "B"[:] * B + "R"[:] * R + "Y"[:] * Y]
		for y in a:
			x = y[:]
			c, v = anss(x[:N/2], x[N/2:])
			if valid(c):
				ans = c
				break
			if valid(v):
				ans = v
				break
		if not valid(ans) or ans.count('R') != R or ans.count('Y') != Y or ans.count('B') != B:
			print 1/0
	print "Case #" + str(t) + ": " + ans