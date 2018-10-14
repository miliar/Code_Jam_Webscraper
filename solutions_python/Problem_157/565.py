
class node:
	def __init__(self, sign, num):
		self.sign = sign
		self.num = num
	def __mul__(self, other):
		sign = self.sign * other.sign
		num = 1
		if self.num == 1:
			num = other.num
		elif self.num == 'i':
			if other.num == 1:
				num = 'i'
			elif other.num == 'i':
				sign *= -1
				num = 1
			elif other.num == 'j':
				num = 'k'
			elif other.num == 'k':
				sign *= -1
				num = 'j'
		elif self.num == 'j':
			if other.num == 1:
				num = 'j'
			elif other.num == 'i':
				sign *= -1
				num = 'k'
			elif other.num == 'j':
				sign *= -1
				num = 1
			elif other.num == 'k':
				num = 'i'
		elif self.num == 'k':
			if other.num == 1:
				num = 'k'
			elif other.num == 'i':
				num = 'j'
			elif other.num == 'j':
				sign *= -1
				num = 'i'
			elif other.num == 'k':
				sign *= -1
				num = 1
		return node(sign, num)


T = int(raw_input())

for case in xrange(1, T + 1):

	l, x = map(int, raw_input().split())
	s = raw_input()
	s *= x
	dp = [0] * len(s)
	dp[0] = node(1, s[0])
	rec = 0

	if dp[0].sign == 1 and dp[0].num == 'i':
		rec = 1

	for i in xrange(1, len(s)):
		dp[i] = dp[i - 1] * node(1, s[i])
		if rec == 0 and dp[i].sign == 1 and dp[i].num == 'i':
			rec = 1
		elif rec == 1 and dp[i].sign == 1 and dp[i].num == 'k':
			rec = 2
	if rec == 2 and dp[-1].sign == -1 and dp[-1].num == 1:
		ans = 'YES'
	else:
		ans = 'NO'

	print 'Case #%d: %s' % (case, ans)