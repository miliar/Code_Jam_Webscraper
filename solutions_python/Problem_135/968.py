class MagicTrick:
	def __init__(self):
		self.firstGrid = []
		self.secondGrid = []
		self.firstAnswer = 0;
		self.secondAnswer = 0;
		self.caseNumber = 1;
		self.text = '';

	def appendFirst(self, row):
		row = row.split(' ', 3)
		row[3] = row[3][:-1]
		self.firstGrid.append(row)

	def appendSecond(self, row):
		row = row.split(' ', 3)
		row[3] = row[3][:-1]
		self.secondGrid.append(row)

	def answerFirst(self, answer):
		self.firstAnswer = answer-1;

	def answerSecond(self, answer):
		self.secondAnswer = answer-1;

	def magic(self):
		matchCard = 0
		matchNumber = 0
		for card in self.firstGrid[self.firstAnswer]:
			if card in self.secondGrid[self.secondAnswer]:
				matchCard = int(card)
				matchNumber=matchNumber+1

		self.trick(matchCard, matchNumber)

	def trick(self, matchCard, matchNumber):
		if(matchNumber == 1): self.text = self.text+('Case #%d: %d\n'%(self.caseNumber, matchCard))
		elif(matchNumber == 0): self.text = self.text+('Case #%d: Volunteer cheated!\n'%(self.caseNumber))
		elif(matchNumber > 1): self.text = self.text+('Case #%d: Bad magician!\n'%(self.caseNumber))

	def reset(self, caseNumber):
		self.firstGrid = []
		self.secondGrid = []
		self.firstAnswer = 0;
		self.secondAnswer = 0;
		self.caseNumber = caseNumber;

if __name__ == "__main__" :
	magicTrick = MagicTrick()
	with open('A-small-attempt0.in', 'r') as testCaseFile:
		totalTestCase = int(testCaseFile.readline())
		for testCase in range(totalTestCase):
			magicTrick.answerFirst(int(testCaseFile.readline()))
			magicTrick.appendFirst(testCaseFile.readline())
			magicTrick.appendFirst(testCaseFile.readline())
			magicTrick.appendFirst(testCaseFile.readline())
			magicTrick.appendFirst(testCaseFile.readline())

			magicTrick.answerSecond(int(testCaseFile.readline()))
			magicTrick.appendSecond(testCaseFile.readline())
			magicTrick.appendSecond(testCaseFile.readline())
			magicTrick.appendSecond(testCaseFile.readline())
			magicTrick.appendSecond(testCaseFile.readline())
			magicTrick.magic()
			magicTrick.reset(testCase+2)
	with open('MagicTrick.out', 'w+') as outPut:
		outPut.write(magicTrick.text)
