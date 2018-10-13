t = input()
for i in range(t):
	print "Case #%d:" % (i + 1),
	n, x = map(int, raw_input().split())
	s = map(int, raw_input().split())
	s = sorted(s)
	z = 0
	l = 0
	r = n - 1
	while l <= r:
		z += 1
		if l < r and s[r] + s[l] <= x:
			l += 1
		r -= 1
	print z