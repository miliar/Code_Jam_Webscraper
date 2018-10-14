#!user/bin/python

inputPath = "warLargeInput.txt"


class Hand:
	def __init__(self, numberOfBlocks, weightOfBlocks):
		self.numberOfBlocks = numberOfBlocks
		self.weightOfBlocks = weightOfBlocks
	def chooseHighestWeight(self):
		return max(self.weightOfBlocks)
	def chooseLightestBlock(self):
		return min(self.weightOfBlocks)
	def findBlockHeavierThan(self, weightInput):
		eligible = []
		for weight in self.weightOfBlocks:
			if weightInput < weight:
				eligible.append(weight)
		blockToReturn = min(eligible)
		self.weightOfBlocks.remove(blockToReturn)
		return blockToReturn
	def returnHeaviestBlock(self):
		heaviestBlock = self.chooseHighestWeight()
		self.numberOfBlocks-=1
		self.weightOfBlocks.remove(heaviestBlock)
		return heaviestBlock
	def returnLightestBlock(self):
		lightestBlock = self.chooseLightestBlock()
		self.numberOfBlocks -= 1
		self.weightOfBlocks.remove(lightestBlock)
		return lightestBlock 
	def containsHeaveirWeight(self, hand):
		containsHeavier = False
		for weight in hand.weightOfBlocks:
			if weight > self.chooseHighestWeight():
				containsHeavier = True
		return containsHeavier



class WarGame:
	def __init__(self, numberOfBlocks, naomiHand, kenHand):
		self.naomiHand = naomiHand
		self.kenHand = kenHand
		self.numberOfBlocks = numberOfBlocks
		self.naomiScore = 0
	def playGame(self):
		while self.numberOfBlocks > 0:
			if(self.playRound() == True):
				self.naomiScore += 1
			self.numberOfBlocks -= 1
		return self.naomiScore
	def playRound(self):
		naomiChoice = self.naomiHand.returnHeaviestBlock()
		kensHighestWeight = self.kenHand.chooseHighestWeight()
		if kensHighestWeight < naomiChoice:
			kenChoice = self.kenHand.returnLightestBlock()
		else:
			kenChoice = self.kenHand.findBlockHeavierThan(naomiChoice)
		if kenChoice < naomiChoice:
			return True
		else:
			return False

class DeceitfulWarGame:
	def __init__(self, numberOfBlocks, naomiHand, kenHand):
		self.naomiHand = naomiHand
		self.kenHand = kenHand
		self.numberOfBlocks = numberOfBlocks
		self.naomiScore = 0
	def playGame(self):
		while self.numberOfBlocks > 0:
			if(self.playRound() == True):
				self.naomiScore += 1
			self.numberOfBlocks -= 1
		return self.naomiScore
	def playRound(self):

		kenHasHeavier = self.naomiHand.containsHeaveirWeight(self.kenHand)
		if kenHasHeavier:
			naomiChoice = self.naomiHand.returnLightestBlock()
		else:
			naomiChoice = self.naomiHand.returnHeaviestBlock()
		kenChoice = self.kenHand.returnHeaviestBlock()
		if kenChoice < naomiChoice:
			return True
		else:
			return False


def processInput(inputPath):
	f = open(inputPath)
	numberOfGames = f.readline()
	lines = f.readlines()

	games = []
	deceitfulGames = []

	for game in range(int(numberOfGames)):
		offset = game * 3
		numberOfBlocks = int(lines[offset])
		naomisHand = map(float, lines[offset+1].split())
		kensHand = map(float, lines[offset+2].split())


		naomiHonestHand = Hand(numberOfBlocks, list(naomisHand))
		kenHonestHand = Hand(numberOfBlocks, list(kensHand))
		honestGame = WarGame(numberOfBlocks, naomiHonestHand, kenHonestHand)
		games.append(honestGame)


		naomiDishonestHand = Hand(numberOfBlocks, list(naomisHand))
		kenDishonestHand = Hand(numberOfBlocks, list(kensHand))
		deceitfulGame = DeceitfulWarGame(numberOfBlocks, naomiDishonestHand, kenDishonestHand)
		deceitfulGames.append(deceitfulGame)

	return deceitfulGames, games

f = open("warLargeOutput.txt", "w")

deceitfulGames, games =  processInput(inputPath)
for idx, game in enumerate(games):
	disHonestResult = str(deceitfulGames[idx].playGame())
	honestResult = str(game.playGame())
	f.write("Case #" + str(idx+1) + ": " + disHonestResult + " " + honestResult + "\n")
f.close()

