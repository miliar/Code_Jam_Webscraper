TC = int(input())
for tc in range(TC):
	S, K = input().split()
	S = [x == '+' for x in S]
	K = int(K)
	ans = 0
	for i in range(len(S)):
		if not S[i]:
			if i+K <= len(S):
				ans += 1
				for j in range(i, i+K):
					S[j] = not S[j]
			else:
				ans = 'IMPOSSIBLE'
				break
	print("Case #%d: %s" % (tc+1, ans))
