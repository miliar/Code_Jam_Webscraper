def winning(S):
	winner = [S[0]]
	length = len(S)
	for i in xrange(length-1):
		if ord(S[i+1]) >= ord(winner[0]):
			winner.insert(0, S[i+1])
		else:
			winner.append(S[i+1])
	return "".join(winner)

#Get input
t = int(raw_input().strip())
tests = []
for _ in xrange(t):
	tests.append(raw_input().strip())
	
#do stuff
for i in xrange(t):
	word = winning(tests[i])
	print "Case #{0}: {1}".format(i+1, word)
