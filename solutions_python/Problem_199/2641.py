for _ in range(1, int(input()) + 1):
	s, k = input().split()
	k = int(k)
	s = [int(c == '+') for c in s]

	result = 0
	for i in range(len(s) - k + 1):
		if s[i] == 0:
			result += 1
			for j in range(k):
				s[i + j] = 1 - s[i + j]

	if sum(s) != len(s):
		result = 'IMPOSSIBLE'

	print('Case #{}: {}'.format(_, result))
