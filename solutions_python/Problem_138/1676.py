from copy import copy as cpy

fi = open("d-in.txt")


def getWar(nblocks, kblocks, n):
	score = 0

	for i in range(n):
		nchosen = min(nblocks)

		largerks = filter(lambda e: e > nchosen, kblocks)
		kchosen = min(largerks) if len(largerks) > 0 else min(kblocks)

		if nchosen > kchosen:
			score += 1

		nblocks.remove(nchosen)
		kblocks.remove(kchosen)

	return score

def getDeceivingWar(nblocks, kblocks, n):
	score = 0

	for i in range(n):
		nchosen = min(nblocks)
		if(min(nblocks) < min(kblocks)):
			ntold = max(kblocks)-0.000001
		else:
			ntold = max(kblocks)+0.000001



		largerks = filter(lambda e: e > ntold, kblocks)
		kchosen = min(largerks) if len(largerks) > 0 else min(kblocks)

		if nchosen > kchosen:
			score += 1

		nblocks.remove(nchosen)
		kblocks.remove(kchosen)

	return score


for problem in range(int(fi.readline())):
	n = int(fi.readline())
	nblocks = map(float, fi.readline().split(" "))
	kblocks = map(float, fi.readline().split(" "))

	print "Case #%d: %d %d" % (problem+1,
														getDeceivingWar(cpy(nblocks), cpy(kblocks), n),
														getWar(cpy(nblocks), cpy(kblocks), n))
	



