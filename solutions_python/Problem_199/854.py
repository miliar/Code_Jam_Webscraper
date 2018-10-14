def convert(S):
	res = []
	for s in S:
		res.append(True if s == '+' else False)
	return res

def solve(S, K):
	cnt = 0
	length = len(S)
	for i in range(length - K + 1):
		if not S[i]:
			for j in range(i, i + K):
				S[j] ^= True
			cnt += 1
	if False not in S: return str(cnt)
	else: return 'IMPOSSIBLE'

f = open(‘A.txt’, ‘w’)
for _ in range(int(input().strip())):
	S, K = input().strip().split()
	f.write('Case #' + str(_ + 1) + ': ' + solve(convert(S), int(K)))
f.close()
