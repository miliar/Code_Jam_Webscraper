#inputs are sorted
def war(nBlocks, kBlocks):
	nScore = 0
	for n in nBlocks:
		toPlay = None
		for k in kBlocks:
			if k > n:
				toPlay = k
				break
		if toPlay:
			kBlocks.remove(toPlay)
		else:
			nScore += 1
			kBlocks = kBlocks[1:]
	return nScore

#inputs are sorted
def deceitfulWar(nBlocks, kBlocks):
	score = 0
	while len(nBlocks) > 1:
		if kBlocks[-1] > nBlocks[-1] or nBlocks[0] < kBlocks[0]:
			nBlocks = nBlocks[1:]
			kBlocks = kBlocks[:-1]
		else:
			score += 1
			nBlocks = nBlocks[1:]
			kBlocks = kBlocks[1:]
	return score + int(nBlocks[0] > kBlocks[0])

from sys import stdin

input = stdin.read().split('\n')

for t in range(int(input[0])):
	nBlocks = sorted(map(float, input[3 * t + 2].split()))
	kBlocks = sorted(map(float, input[3 * t + 3].split()))

	print "Case #{0}: {1} {2}".format(t+1, deceitfulWar(nBlocks, kBlocks), war(nBlocks, kBlocks))