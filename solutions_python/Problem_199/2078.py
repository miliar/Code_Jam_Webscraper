f = open('./input', 'r')
lines = f.readlines()
nt = int(lines[0])
for t in range(nt):
	sk = lines[t + 1].split(' ')
	s = [x for x in sk[0]]
	k = int(sk[1])
	ans = 0
	for i in range(len(s)):
		if i + k - 1 >= len(s):
			break
		if s[i] == '-':
			ans += 1
			for j in range(k):
				if s[i + j] == '-':
					s[i + j] = '+'
				else:
					s[i + j] = '-'
	ok = True
	for i in range(len(s)):
		if s[i] == '-':
			ok = False
			break
	if ok:
		print('Case #{0}: {1}'.format(t + 1, ans))
	else:
		print('Case #{0}: IMPOSSIBLE'.format(t + 1))