t = int(input())

for tc in range(t):
	tc += 1
	s = input()
	tidy = [int(i) for i in s[::-1]]
	
	for i in range(1, len(tidy)):
		if tidy[i] > tidy[i - 1]:
			tidy[i] -= 1
			for j in range(i):
				tidy[j] = 9

	tidy = [str(i) for i in tidy]
	print('Case #{}: {}'.format(tc, int(''.join(tidy)[::-1])))
