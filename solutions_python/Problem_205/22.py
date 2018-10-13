from collections import deque

initial_hd = None
b,d = None, None

def Valid(hd, hk, ad, ak):
	if hk <= 0: return 1
	if hd <= 0: return -1
	if ad >= 200: return -1
	if ak <= -d: return -1
	return 0

def getAdjs(hd, hk, ad, ak):
	return [
		(hd-ak, hk-ad, ad, ak), #Attack
		(hd-ak, hk, ad+b, ak), #Buff
		(initial_hd-ak, hk, ad, ak), #Cure
		(hd-(ak-d), hk, ad, ak-d) #Debuff
	]


def solve():
	global b
	global d
	global initial_hd
	hd, ad, hk, ak, b, d = map(int, raw_input().split())
	initial_hd = hd
	dp = {}
	dp[(hd, hk, ad, ak)] = 0
	queue = deque([(hd, hk, ad, ak)])
	while len(queue) > 0:
		first = queue.popleft()

		valid = Valid(*first)
		if valid == 1:
			return dp[first]
		elif valid == -1:
			continue

		adjs = getAdjs(*first)
		for adj in adjs:
			if adj not in dp:
				dp[adj] = dp[first]+1
				queue.append(adj)

	return "IMPOSSIBLE"





t = int(raw_input())

for testNum in range(t):
	print "Case #{}: {}".format(testNum+1, solve())