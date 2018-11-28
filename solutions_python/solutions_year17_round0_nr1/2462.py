t = 0
t = int(input())
outcome = ''
for test in range(t):
	maxnum = 9999999999999999
	line = input().strip().split()
	s = list(line[0])
	for i in range(len(s)):
		if s[i] == '-': s[i] = False
		else: s[i] = True
	k = int(line[1])
	if False not in s:
		outcome = 0
	else:
		flips = 0
		for flip in range(len(s)-k+1):
			if not s[flip]:
				for i in range(k):
					s[flip+i] = not s[flip+i]
				flips += 1
		if False in s:
			outcome = 'IMPOSSIBLE'
		else:
			outcome = flips
	print("Case #{0}: {1}".format(test+1, outcome))
