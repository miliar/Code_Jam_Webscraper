T = int(input())

for i in range(1, T+1):
	S, K = input().split()
	S = list(S)
	K = int(K)
	result = "IMPOSSIBLE"
	count = 0
	for c in range(len(S) - K + 1):
		if S[c] == "-":
			for j in range(K):
				S[c+j] = "+" if S[c+j] == "-" else "-"
			count += 1
	if all(c == "+" for c in S):
		result = count
	print(f"Case #{i}: {result}")
