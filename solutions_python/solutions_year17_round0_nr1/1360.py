def flip(s, k):
	chips = list(s)
	count = 0
	i = 0
	while i < len(chips):
		if chips[i] == '-':
			if i + k <= len(chips):
				for j in range(i + 1, i + k):
					if chips[j] == '+':
						chips[j] = '-'
					else:
						chips[j] = '+'
				count += 1
			else:
				return -1
		i += 1

	return count

n = int(input())
for i in range(n):
	s, k = input().split(' ')
	result = flip(s, int(k))
	if result == -1:
		print('Case #{}: IMPOSSIBLE'.format(i + 1))
	else:
		print('Case #{}: {}'.format(i + 1, result))
