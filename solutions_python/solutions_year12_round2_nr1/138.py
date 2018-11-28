import sys, math
debug = sys.stdout

sys.stdin  = open('A-large.in')
sys.stdout = open('A.out', 'w')

#Not working because some contestants have an excess of votes

for j in xrange(input()):
	scores = [int(x) for x in raw_input().split(' ')]
	scores = scores[1:]

	startScores = []
	startScores[:] = scores
	total = sum(scores)

	pointsToGive = total

	threshold = 0
	while pointsToGive > 0:
		needed = 0
		for s in scores:
			if s < threshold:
				needed += 1

		if pointsToGive >= needed:
			for i, s in enumerate(scores):
				if s < threshold:
					scores[i] = threshold
		else:
			for i, s in enumerate(scores):
				if s < threshold:
					scores[i] += float(pointsToGive) / needed

		pointsToGive -= needed
		threshold += 1



	votesNeeded = [(end - start) for start, end in zip(startScores, scores)]

	print >> debug, startScores, sum(startScores)
	print >> debug, votesNeeded, sum(votesNeeded)
	print >> debug, scores
	print >> debug
	print 'Case #%d: %s' % (j+1, ' '.join('%.6f' % (100 * v / float(total)) for v in votesNeeded))