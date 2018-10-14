t = input()

for qe in range(1, t+1):
	
	s, k = raw_input().split()
	s = list(s)
	k = int(k)

	cnt = 0

	for i in range(len(s)-k+1):
		if s[i] == '-':
			cnt += 1
			for j in range(i, i+k):
				if s[j] == '-':
					s[j] = '+'
				else:
					s[j] = '-'


	if not all(i == '+' for i in s):
		cnt = 'IMPOSSIBLE'


	print 'Case #{}: {}'.format(qe, cnt)