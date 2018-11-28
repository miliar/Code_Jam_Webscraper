T = int(input())
for t in range(1, T + 1):
	result = 0
	S, K = [s for s in input().split(" ")]
	K = int(K)
	
	S = [0 if x == "-" else 1 for x in S]
	
	if 0 in S:
		for i in range(len(S)):
			if S[i] == 0 and i+K <= len(S):
				result += 1
				for j in range(i, i+K):
					S[j] = 1 - S[j]
		if 0 in S:
			result = "IMPOSSIBLE"
	print("Case #{}: {}".format(t, result))