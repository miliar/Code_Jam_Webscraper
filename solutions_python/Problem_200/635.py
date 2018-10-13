def iterate(n,digits):
	ns = list(str(n))
	if ns == sorted(ns):
		digits.append(ns[-1])
		return n/10
	else:
		digits.append('9')
		return n/10-1



def solve(ip = None):
	n = ip or input()
	digits = []
	while n>0:
		n = iterate(n,digits)
	digits = digits[::-1]
	return ''.join(digits)


if __name__ == '__main__':
	t = input()
	c = 1
	while c<=t:
		print 'Case #{}: {}'.format(c,solve())
		c+=1

	'''
	# Test output correctness for inputs in range 1 to 100000
	dp = [-1 for i in xrange(100001)]
	for i in range(1,100001):
		if i < 10:
			dp[i] = i
		else:
			ns = list(str(i))
			dp[i] = i if ns == sorted(ns) else dp[i-1]

		try:
			assert(dp[i] == int(solve(i)))
		except:
			print i,dp[i],solve(i)
			break
	'''
