def my(s):
	x = int(s)
	s = list(s)
	n = len(s)
	stop = n
	ans = x
	for i in range(1, n):
		if s[i - 1] > s[i]:
			stop = i - 1
			break
	if stop != n:
		for i in range(stop, 0, -1):
			if s[i] != s[i - 1]:
				stop = i
				break
		else:
			stop = 0
		s[stop] = str(int(s[stop]) - 1)
		for i in range(stop + 1, n):
			s[i] = '9'
		ans = int(''.join(s))
	return ans
for test in range(1, int(input()) + 1):
	ans = my(input())
	print("Case #%d: %d" % (test, ans))