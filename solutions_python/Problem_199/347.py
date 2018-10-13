import sys

T = int(sys.stdin.readline())
for case_number in range(1, T+1):
	s, K_str = sys.stdin.readline().split()
	K = int(K_str)
	n = len(s)
	S = list(map(lambda x : 1 if x=='+' else 0, s))

	count = 0
	for i in range(0, n - K + 1):
		if S[i] == 0:
			count += 1
			for j in range(i, i+K):
				S[j] = 1 - S[j]

	impossible = any(x == 0 for x in S[n-K+1:])

	print("Case #{}: {}".format(case_number, "IMPOSSIBLE" if impossible else count))
