def min_nbr_flips(S, K):
	nbr_flips = 0
	for j in range(len(S)-(K-1)):
		if not S[j]:
			nbr_flips += 1
			for k in range(j+1, j+K):
				S[k] = not S[k]
	if all(S[-(K-1):]):
		return str(nbr_flips)
	else:
		return 'IMPOSSIBLE'

N = int(input())
for j in range(N):
	(S, K) = input().split(" ")
	K = int(K)
	S = [ch=='+' for ch in S]
	res = min_nbr_flips(S, K)
	print("Case #%d: %s" % (j+1, res))
