
K = 10

x = [ [ 0  for j in range(10) ] for k in range(K) ]
acs = [ 0 for k in range(K) ]
for d in range(1, 10):
	x[1][d] = 1
	acs[1] += x[1][d]
for k in range(2, K):
	for d in range(1, 10):
		for i in range(d, 10):
			x[k][d] += x[k - 1][i]
		acs[k] += x[k][d]


def acsum(a):
	n = len(a)
	m = len(a[0])
	acs = [ [ 0  for j in range(m) ] for i in range(n) ]
	acs[1][1] = a[1][1]
	for j in range(2, m):
		acs[1][j] = acs[1][j - 1] + a[1][j]
	for i in range(2, n):
		acs[i][1] = acs[i - 1][1] + a[i][1]
	for i in range(2, n):
		for j in range(2, m):
			acs[i][j] = acs[i - 1][j] + acs[i][j - 1] - acs[i - 1][j - 1] + a[i][j]
	return acs

# get minimum k such that acs[k] >= n
def get_kn(n):
	lb = 1
	ub = K - 1
	while ub - lb > 1:
		mid = (lb + ub) // 2
		if acs[mid] > n:
			ub = mid
		else:
			lb = mid + 1
	if acs[lb] > n:
		return lb
	return ub

def find(N):
	sumprev = 0
	sum = 0
	for k in range(1, K):
		for d in range(1, 10):
			sumprev = sum
			sum += x[k][d]
			if N <= sum:
				return k, d, sumprev
	return None

def solve(N):
	k, d, sum = find(N)
	print(k)
	print(d)
	print(sum)
	print(sum + x[k][d])
	ans = [ 0 for i in range(k) ]
	ans[0] = d
	for i in range(1, k):
		N -= sum
		k, d, sum = find(N)
		ans[i] = d
	return ans

def solve_brute(N):
	while not good(N):
		N -= 1
	return N

def good(x):
	s = str(x)
	for i in range(1, len(s)):
		if int(s[i - 1]) > int(s[i]):
			return False
	return True

def solve_fast(N):
	d = [ int(x) for x in str(N) ]
	ans = [ 0 ] * len(d)
	j = -1
	for i in range(0, len(d)):
		ans[i] = d[i]
		if i + 1 < len(d) and d[i + 1] < d[i]:
			j = i 
			break
	if j == -1:
		return format(ans)
	while j - 1 >= 0 and ans[j - 1] == ans[j]:
		j -= 1
	ans[j] -= 1
	for i in range(j + 1, len(d)):
		ans[i] = 9
	return format(ans)

def format(ans):
	i = 0
	while ans[i] == 0:
		i += 1
	s = ''
	for j in range(i, len(ans)):
		s += str(ans[j])
	return s

#print(10000)
#for i in range(10000):
#	print(i + 1)
#exit(0)

f = open('./input', 'r')
lines = f.readlines()
nt = int(lines[0])
for tc in range(1, nt + 1):
	N = int(lines[tc])
	ans = solve_fast(N)
	print('Case #{0}: {1}'.format(tc, ans))