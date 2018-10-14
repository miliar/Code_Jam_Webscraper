import fractions
def factor(n):  
	if n == 1: return [1]  
	m = n**0.5 + 1 
	k = 2  
	while k < m:  
		if n % k == 0:
			ret = factor(n/k)
			ret.append(k)
			return ret
		k += 1

	return [n]  

TESTCASES = int(raw_input())

for CASE in range(TESTCASES):
	T = map(int, raw_input().split(' '))
	N = T[0]
	T = T[1:]

	gcf = (T[0]-T[1])
	for x in range(N):
		for y in range(x+1, N):
			gcf = fractions.gcd(gcf, abs(T[x]-T[y]))

	# All meet the factors

	m = gcf
	TIME = 0
	while True:
		INC = [0] * N
		for x in range(N):
			i = (T[x] % m)
			if i > 0: i = m-i
			INC[x] = i
		mx = max(INC)
		TIME += mx
		if min(INC) == mx: break
		T = [k+mx for k in T]
  
	
	print "Case #%d: %d" % (CASE+1, TIME)
