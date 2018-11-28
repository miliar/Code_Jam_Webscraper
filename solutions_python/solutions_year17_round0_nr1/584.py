import sys

sys.setrecursionlimit(4000)

def solve(pancakes, K):
	if len(pancakes) < K:
		for p in pancakes:
			if p == -1:
				return -1
		return 0
	else:
		if pancakes[0] == 1:
			return solve(pancakes[1:], K)
		else:
			for i in range(K):
				pancakes[i] = -1*pancakes[i]
			rec = solve(pancakes[1:], K)
			if (rec == -1):
				return -1
			else: 
				return 1 + rec

T = int(raw_input())

for i in range(T):
	s, K = raw_input().split()
	K = int(K)
	s = list(s)
	for j in range(len(s)):
		if s[j] == '+':
			s[j] = 1
		else:
			s[j] = -1
	res = solve(s, K)
	if res == -1:
		res = "IMPOSSIBLE"
	else:
		res = str(res) 
	print("Case #%d: %s"%(i+1, res))

