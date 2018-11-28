T = int(input())

for t in range(T):
	#print(t)
	S, K = str(input()).split(' ')
	S = list(S)
	K = int(K)

	res = 0
	#print(S)
	for i in range(len(S)):
		if S[i] == '+':
			continue
		else:
			res += 1
			if (i+K-1) > (len(S) - 1):
				res = -1
				break

			for k in range(K):
				if S[i+k] == '-':
					S[i+k] = '+'
				else:
					S[i+k] = '-'
			#print(S)

	s_res = str(res)
	if res == -1:
		s_res = "IMPOSSIBLE"
	print("Case #{}: {}".format(t+1, s_res))