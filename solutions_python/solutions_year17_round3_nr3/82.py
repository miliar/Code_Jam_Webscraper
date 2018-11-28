'''input
4
4 4
1.4000
0.5000 0.7000 0.8000 0.6000
2 2
1.0000
0.0000 0.0000
2 1
0.0000
0.9000 0.8000
2 1
0.1000
0.4000 0.5000
'''
def up(P, U, m):
	for i in range(m, len(P)):
		if i + 1 < len(P):
			d = P[i+1] - P[i]
		else:
			d = 1.0 - P[i]
		add = min(d, U / (i - m + 1))
		for k in range(m, i+1):
			P[k] += add
			U -= add
		if U <= 0.0:
			break
	return P
 
def down(P, U):
	for i in range(len(P)-1, -1, -1):
		if P[i] + U >= 1.0:
			U -= 1.0 - P[i]
			P[i] = 1.0
		if U <= 0.0:
			break
	return P

def calc_dp(P, k_min):
	n = len(P)
	dp = []
	for _ in range(n+1):
		dp.append([0.0] * (n + 1))
	
	dp[0][0] = 1.0
	for k in range(n+1):
		for i in range(1,n+1):
			p = 0.0
			p += dp[k][i-1] * (1.0 - P[i-1])
			
			if k > 0:
				p += dp[k-1][i-1] * P[i-1]
 
			dp[k][i] = p
 
	res = 0.0
	for k in range(k_min, n+1):
		res += dp[k][n]

	return res
 
def solve(K, U, P):
	best = 0.0

	for x in [False, True]:
		p = sorted(list(P))
		rem = U

		if x:
			p = down(p, rem)
			rem = sum(P) + U - sum(p)

		for start_index in range(len(P)):
			t = up(list(p), rem, start_index)
			best = max(best, calc_dp(t, K))
	
	return best
 

T = int(input())
for t in range(T):
	N, K = map(int, input().split())
	U = float(input())
	P = list(map(float, input().split()))	

	res = solve(K, U, P)

	print('Case #{}: {:.6f}'.format(t + 1, res))
