import codejam as gcj

T = gcj.read_input('i')
for t in range(T):
	S, K = gcj.read_input('s i')
	S = list(S)
	
	flip, flips = {'+':'-', '-':'+'}, 0
	for i in range(len(S) - K + 1):
		if S[i] == '-':
			flips += 1
			S[i:i + K] = [flip[s] for s in S[i:i + K]]
	
	if '-' in S:
		answer = 'IMPOSSIBLE'
	else:
		answer = flips
	
	print 'Case #%i:' % (t + 1), answer
