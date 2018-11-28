import sys

T = int(sys.stdin.readline())
for case_number in range(1, T+1):
	N = list(map(int, sys.stdin.readline().strip()))

	for i in range(1, len(N)):
		if N[i] < N[i-1]:
			t = N[i-1]
			first = N.index(N[i-1])
			for j in range(first+1, len(N)):
				N[j] = 9
			N[first] = t-1
			break

	answer = int("".join(str(x) for x in N))
	print("Case #{}: {}".format(case_number, answer))

