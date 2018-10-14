t = int(raw_input())

combs = []
for i in xrange(501):
	combs.append(501*[-1])

def comb(n,k):
	if combs[n][k] > 0:
		return combs[n][k]
	a, b = min(n-k, k), max(n-k, k)
	answer = 1
	for i in xrange(b+1,n+1):
		answer *= i
	for j in xrange(2,a+1):
		answer /= j
	combs[n][k] = answer
	return answer

total = 501*[0]
dp = []
for j in xrange(501):
	dp.append((501)*[0])
for j in xrange(501):
	dp[j][0] = 1
for j in xrange(2,501):
	for m in xrange(1,j-1):
		for k in xrange(max(0,2*m-j+1),m):
			dp[j][m] += dp[m+1][k] * comb(j-m-2, m-k-1)
			dp[j][m] %= 100003
	for x in dp[j]:
		total[j]+=x
		total[j]%=100003

for i in xrange(t):
	n = int(raw_input())
	print "Case #%d: %d" % (i+1,total[n])
