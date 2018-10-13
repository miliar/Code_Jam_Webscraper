def probD():

	filename = "D-large.in.txt"
	f = open(filename)
	cases, results = int(f.readline()), []
	for i in range(cases):
		numBlocks = f.readline()
		nBlocks = [float(x) for x in f.readline().split()]
		kBlocks = [float(x) for x in f.readline().split()]

		nBlocks.sort()
		kBlocks.sort()

		deceitPoints = playDeceitfulWar([x for x in nBlocks], [x for x in kBlocks])
		truthPoints = playWar(nBlocks, kBlocks)
		print deceitPoints, truthPoints
		results.append("%i %i" % (deceitPoints, truthPoints))
	writeResults(results)
		

def decideKenChoice(naomiTold, ken):

	if naomiTold < min(ken):
		return min(ken)
	if naomiTold > max(ken):
		return min(ken)

	choices = [x for x in ken if x > naomiTold]
	return min(choices)

def playWar(naomi, ken):

	points = 0
	while naomi:
		naomiChosen = min(naomi)
		kenChosen = decideKenChoice(naomiChosen, ken)

		if naomiChosen > kenChosen:
			points += 1

		naomi.remove(naomiChosen)
		ken.remove(kenChosen)

	return points

def playDeceitfulWar(naomi, ken):

	points = 0
	while naomi:

		# naomi wants to force ken to play his largest block
		kMin, kMax = min(ken), max(ken)
		nMin, nMax = min(naomi), max(naomi)

		if nMin > kMin: # deceive to make ken play the smallest - still get point
			nTold = kMax + 0.0000001
			nChosen = nMin
			kChosen = decideKenChoice(nTold, ken)
		elif nMin < kMin and len(ken) > 1: # force ken to play the largest - lose point
			nTold = max(x for x in ken if x != kMax) + 0.0000001 # second largest
			nChosen = nMin
			kChosen = decideKenChoice(nTold, ken)
		else:
			nChosen = nMax
			kChosen = decideKenChoice(nChosen, ken)

		if nChosen > kChosen:
			points += 1

		'''
		print nChosen, kChosen
		print "N:" + str(naomi), sum(naomi)
		print "K:" + str(ken), sum(ken)
		print
		'''
		# remove blocks
		naomi.remove(nChosen)
		ken.remove(kChosen)

	return points


def writeResults(results):
	outfile = open("probDResults.txt", "w")
	for i in range(1, len(results) + 1):
		outfile.write("Case #%i: %s\n" % (i, results[i-1]))
	outfile.close()

probD()