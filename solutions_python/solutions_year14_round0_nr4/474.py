EPSILON = 1e-6

def main():

	numTestCases = int(raw_input())

	for n in xrange(numTestCases):
		numBlocks = int(raw_input())

		naomiBlocks = map(float, raw_input().split())
		kenBlocks = map(float, raw_input().split())

		naomiBlocks.sort()
		kenBlocks.sort()

		# print "Naomi: ", naomiBlocks
		# print "Ken: ", kenBlocks

		naomiWarScore = war(list(naomiBlocks), list(kenBlocks))
		naomiDeceitScore = deceit(list(naomiBlocks), list(kenBlocks))

		print "Case #{}: {} {}".format(n+1, naomiDeceitScore, naomiWarScore)


def deceit(naomiBlocks, kenBlocks):

	numRounds = len(naomiBlocks)

	naomiScore = 0
	for n in xrange(numRounds):
		# Option 1 - Naomi's smallest is larger than Ken's biggest
		# Option 2 - Naomi's smallest is smaller than Ken's biggest

		chosenNaomi = naomiBlocks[0]
		chosenKen = kenBlocks[0]

		# Option 2
		# if chosenNaomi < max(kenBlocks):
		# 	toldNaomi = max(kenBlocks)-EPSILON
		# else:
		# 	toldNaomi = max(kenBlocks)+EPSILON
		
		if chosenNaomi > min(kenBlocks):
			toldNaomi = max(kenBlocks)+EPSILON
		else:
			toldNaomi = max(kenBlocks)-EPSILON

		for k in kenBlocks:
			if k > toldNaomi:
				chosenKen = k
				break

		naomiBlocks.remove(chosenNaomi)
		kenBlocks.remove(chosenKen)

		if chosenNaomi > chosenKen:
			naomiScore = naomiScore + 1
	
	return naomiScore


def war(naomiBlocks, kenBlocks):
	
	# print (naomiBlocks, kenBlocks)

	numRounds = len(naomiBlocks)

	# print numRounds
	naomiScore = 0
	for n in xrange(numRounds):
		chosenNaomi = naomiBlocks[0]

		chosenKen = kenBlocks[0]
		# print (chosenKen, chosenNaomi)
		for k in kenBlocks:
			if k > chosenNaomi:
				chosenKen = k
				# print (chosenKen, chosenNaomi)
				break

		naomiBlocks.remove(chosenNaomi)
		kenBlocks.remove(chosenKen)

		if chosenNaomi > chosenKen:
			naomiScore = naomiScore + 1

		# print (naomiBlocks, kenBlocks)

	return naomiScore

if __name__ == "__main__":
	main()