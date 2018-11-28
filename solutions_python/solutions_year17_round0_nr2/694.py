t = input()
def F(x):
	s = str(x)
	for i in range(1, len(s)):
		if s[i] < s[i - 1]:
			ans = int(s[:i] + '0' * (len(s) - i)) - 1
			break
	else:
		ans = int(s)
	return ans
for tt in range(1, t + 1):
	x = input()
	while True:
		y = F(x)
		if x == y:
			break
		x = y
	print 'Case #%d: %d' % (tt, x)