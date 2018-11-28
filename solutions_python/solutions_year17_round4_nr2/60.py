T = int(raw_input())

def doprob():
	N, C, M = map(int, raw_input().split())
	ppl = {}
	pos = {}
	for i in xrange(N):
		pos[i+1] = []
	for i in xrange(M):
		P, B = map(int, raw_input().split())
		if B not in ppl:
			ppl[B] = [P]
		else:
			ppl[B].append(P)
		if P not in pos:
			pos[P] = [B]
		else:
			pos[P].append(B)
	maxscore = 0
	for i in ppl:
		if len(ppl[i]) > maxscore:
			maxscore = len(ppl[i])
	stutter = [0]
	for i in xrange(N):
		stutter.append(stutter[i]+len(pos[i+1]))
	maxscore2 = 0
	for i in xrange(1, N+1):
		if (stutter[i]+i-1)/i > maxscore2:
			maxscore2 = (stutter[i]+i-1)/i
	outscore = max(maxscore, maxscore2)
	out = str(outscore) + " "
	total = 0
	for i in xrange(1, N+1):
		total += max(0, len(pos[i])-outscore)
	return out + str(total)


for qq in xrange(T):
	print "Case #" + str(qq+1) + ": " + str(doprob())