import bisect
from copy import copy, deepcopy

class WarSet:
	def __init__(self):
		self.naomiSet = []
		self.kenSet = []
		self.decietfulWin = 0
		self.warWin = 0;
		self.text = '';
		self.caseNumber = 1;

	def setNaomi(self, naomiSet):
		self.naomiSet = sorted(naomiSet)

	def setKen(self, kenSet):
		self.kenSet = sorted(kenSet)

	def play(self):
		bufferNaomiSet = deepcopy(self.naomiSet)
		bufferKenSet = deepcopy(self.kenSet)
		self.playDecietful()
		self.naomiSet = bufferNaomiSet
		self.kenSet = bufferKenSet
		self.playWar()
		self.text = self.text+('Case #%d: %d %d\n'%(self.caseNumber, self.decietfulWin, self.warWin))

	def playWar(self):
		while(len(self.naomiSet) > 0):
			naomiChosen = self.naomiWarChoose()
			kenChosen = self.kenChoose(naomiChosen)
			if(naomiChosen > kenChosen):
				self.warWin = self.warWin + 1

	def kenChoose(self, naomiTold):
		optimalKen = bisect.bisect(self.kenSet, naomiTold)
		if(optimalKen >= len(self.kenSet)): return self.kenSet.pop(0)
		else: return self.kenSet.pop(optimalKen)

	def naomiWarChoose(self):
		naomiChosen = self.naomiSet[0]
		self.naomiSet = self.naomiSet[1:]
		return naomiChosen

	def playDecietful(self):
		while(len(self.naomiSet) > 0):
			naomiTold, isOptimal, optimalIndex = self.naomiCheat()
			naomiChosen = self.naomiDecietfulChoose(isOptimal, optimalIndex)
			kenChosen = self.kenDecieved(naomiTold)
			if(naomiChosen > kenChosen):
				self.decietfulWin = self.decietfulWin + 1

	def naomiDecietfulChoose(self, isOptimal, optimalIndex):
		if(isOptimal): return self.naomiSet.pop(optimalIndex)
		else:
			naomiChosen = self.naomiSet[0]
			self.naomiSet = self.naomiSet[1:]
			return naomiChosen

	def kenDecieved(self, naomiTold):
		optimalKen = bisect.bisect(self.kenSet, naomiTold)
		if(optimalKen >= len(self.kenSet)): return self.kenSet.pop(-1)
		else: return self.kenSet.pop(optimalKen)

	def naomiCheat(self):
		kenGreatest = self.findKenGreatest()
		naomiOptimal, isOptimal, optimalIndex = self.findNaomiOptimal(kenGreatest)
		if(isOptimal): return naomiOptimal, isOptimal, optimalIndex
		else: return kenGreatest-0.000001, isOptimal, optimalIndex

	def findKenGreatest(self):
		return self.kenSet[-1]

	def findNaomiOptimal(self, kenGreatest):
		optimalNaomi = bisect.bisect(self.naomiSet, kenGreatest)
		if(optimalNaomi >= len(self.naomiSet)): return self.naomiSet[0], False, 0
		else: return self.naomiSet[optimalNaomi], True, optimalNaomi

	def reset(self, caseNumber):
		self.naomiSet = []
		self.kenSet = []
		self.decietfulWin = 0
		self.warWin = 0;
		self.caseNumber = caseNumber;

if __name__ == "__main__" :
	warGame = WarSet()
	with open('D-large.in', 'r') as testCaseFile:
		totalTestCase = int(testCaseFile.readline())
		for testCase in range(totalTestCase):
			totalBlock = int(testCaseFile.readline())
			if(totalBlock == 1):
				warGame.setNaomi([float(testCaseFile.readline()[:-1])])
				warGame.setKen([float(testCaseFile.readline()[:-1])])
			else:
				warGame.setNaomi(map(float, testCaseFile.readline()[:-1].split(' ', totalBlock-1)))
				warGame.setKen(map(float, testCaseFile.readline()[:-1].split(' ', totalBlock-1)))
			warGame.play()
			warGame.reset(testCase+2)
	with open('WarSet.out', 'w+') as outPut:
		outPut.write(warGame.text)
	print 'finished'
