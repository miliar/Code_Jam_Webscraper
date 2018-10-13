T = input()
for i in range(1,T+1):
	stri = raw_input().split()
	S = list(stri[0])
	K = int(stri[1])
	length = len(S)
	count = 0
	for j in range(length):
		if S[j] == '+':
			S[j] = '0'
		else:
			S[j] = '1'
	for j in range(length - K+1):
		if S[j] == '1':
			count += 1
			for l in range(j,j+K):
				if(S[l] == '0'):
					S[l] = '1'
				else:
					S[l] = '0'

	x = True
	for j in range(length):
		if S[j] == '1':
			x = False
	print "Case #%d: " %i,
	if(x):
		print count
	else:
		print "IMPOSSIBLE"