def getP2Value(p1Value, p2Weights, p2UsedWeights):
	for v in p2Weights:
		if v > p1Value and not(v in p2UsedWeights):
			return v

	for v in p2Weights:
		if not(v in p2UsedWeights):
			return v
	return -1

def getWarWins(n, p1Weights, p2Weights):
	p2UsedWeights = set([])
	wins = 0

	for i in range(n):
		p1Value = p1Weights[i]
		p2Value = getP2Value(p1Value, p2Weights, p2UsedWeights)

		if p1Value > p2Value:
			wins += 1
		p2UsedWeights.add(p2Value)

	return wins

def getDeceitfulWarWins(n, p1Weights, p2Weights):
	p2UsedWeights = set([])
	p1DefiniteLosses = [v for v in p1Weights if v < p2Weights[0]]
	wins = 0

	for i in range(len(p1DefiniteLosses)):
		#print("P1 Plays "+str(p1DefiniteLosses[i])+" and P2 plays "+str(p2Weights[len(p2Weights)-1-i]))
		p2UsedWeights.add(p2Weights[len(p2Weights)-1-i])

	for i in range(len(p1DefiniteLosses), n):
		p1Value = p1Weights[i]
		p2Value = getP2Value(0.999999, p2Weights, p2UsedWeights) #Get smallest value

		if p1Value > p2Value:
			wins += 1

		else:
			p2Value = -1
			for i in range(n-1, -1, -1):
				if not p2Weights[i] in p2UsedWeights:
					p2Value = p2Weights[i]
					break

		p2UsedWeights.add(p2Value)
		#print("P1 plays "+str(p1Value)+" and P2 plays "+str(p2Value))

	return wins

def run():
	testCaseCount = eval(input())

	for i in range(testCaseCount):
		blocksPerPlayer = int(eval(input()))
		p1Weights = [eval(s) for s in input().split(' ')]
		p2Weights = [eval(s) for s in input().split(' ')]
		p1Weights.sort()
		p2Weights.sort()

		#print(p1Weights)
		#print(p2Weights)

		warWins = getWarWins(blocksPerPlayer, p1Weights, p2Weights)
		deceitfulWarWins = getDeceitfulWarWins(blocksPerPlayer, p1Weights, p2Weights)
		print("Case #{:d}: {:s} {:s}".format(i+1, str(deceitfulWarWins), str(warWins)))


if __name__ == '__main__':
	run()