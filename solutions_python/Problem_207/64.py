for test in range(1, int(input()) + 1):

	n, r, o, y, g, b, v = map(int, input().split())
	a = [[r, 'R'], [o, 'O'], [y, 'Y'], [g, 'G'], [b, 'B'], [v, 'V']]
	a.sort()
	a.reverse()
	ans = "IMPOSSIBLE"
	if a[0][0] <= a[1][0] + a[2][0]:
		l = a[2][0] + a[1][0] - a[0][0]
		l //= 2
		if a[2][0] >= l:
			# print(a, ans)
			a[1][0] -= l
			a[2][0] -= l
			ans = ''
			ans += (a[1][1] + a[2][1]) * l

			if a[1][0] + a[2][0] > a[0][0]:
				if a[2][0] > 0:
					ans += a[0][1] + a[1][1] + a[2][1]
					a[0][0] -= 1
					a[1][0] -= 1
					a[2][0] -= 1
			
			ans += (a[0][1] + a[1][1]) * a[1][0]
			ans += (a[0][1] + a[2][1]) * a[2][0]
	if len(ans) < n:
		ans = 'IMPOSSIBLE'
	print("Case #%d: %s" % (test, ans))