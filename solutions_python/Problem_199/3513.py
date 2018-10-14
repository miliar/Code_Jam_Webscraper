import sys


class flipPancake():
	leftCounter = 0
	rightCounter = 0
	flipperSize = 0
	stringArray = []

	def startProcessing(self,caseNumber):
		self.leftCounter = 0
		self.rightCounter = len(self.stringArray) - 1
		if self.flipperSize == len(self.stringArray):
			if '-' in self.stringArray and '+' in self.stringArray:
				print 'Case #'+str(caseNumber)+': IMPOSSIBLE'
			elif '-' in self.stringArray:
				print  'Case #'+str(caseNumber)+': 1'
			elif '+' in self.stringArray:
				print  'Case #'+str(caseNumber)+': 0'
		elif '-' not in self.stringArray:
			print  'Case #'+str(caseNumber)+': 0'
		else:
			if '-' not in self.stringArray:
				print  'Case #'+str(caseNumber)+': 0'
			else:
				numSteps = 0
				while '-' in self.stringArray:
					val = self.leftFlip()
					if val == '0':
						print 'Case #'+str(caseNumber)+': IMPOSSIBLE'
						return
					elif val == '2':
						numSteps -= 1
					numSteps += 1
					if '-' in self.stringArray:
						val = self.rightFlip()
						if val == '0':
							print 'Case #'+str(caseNumber)+': IMPOSSIBLE'
							return
						elif val == '2':
							numSteps -= 1
						numSteps += 1
				print 'Case #'+str(caseNumber)+': '+str(numSteps)


	def getCounterVal(self, counter, direction):
		if direction == 'left':
			while counter < len(self.stringArray):
				if self.stringArray[counter] == '-':
					return counter
				else:
					counter += 1
		else:
			while counter > 0:
				if self.stringArray[counter] == '-':
					return counter
				else:
					counter -= 1
		return counter


	def rightFlip(self):
		while self.rightCounter>self.leftCounter:
			if self.stringArray[self.rightCounter] == '-':
				break
			else:
				self.rightCounter -= 1
		if self.rightCounter - self.flipperSize+1 >= self.leftCounter:
			self.flip(self.rightCounter,'right')
			self.rightCounter = self.getCounterVal(self.rightCounter,'right')
			return '1'
		elif self.rightCounter == 0:
			return '2'
		else:
			return '0'


	def leftFlip(self):
		while self.leftCounter<self.rightCounter:
			if self.stringArray[self.leftCounter] == '-':
				break
			else:
				self.leftCounter += 1
		if self.leftCounter + self.flipperSize-1 <= self.rightCounter:
			self.flip(self.leftCounter,'left')
			self.leftCounter = self.getCounterVal(self.leftCounter,'left')
			return '1'
		elif self.leftCounter == len(self.stringArray)-1:
			return '2'
		else:
			return '0'


	def flip(self, position, direction):
		if direction == 'left':
			limit = position + self.flipperSize
			while position < limit:
				if self.stringArray[position] == '-':
					self.stringArray[position] = '+'
				else:
					self.stringArray[position] = '-'
				
				position += 1
		else:
			limit = position - self.flipperSize
			while position > limit:
				if self.stringArray[position] == '-':
					self.stringArray[position] = '+'
				else:
					self.stringArray[position] = '-'
				
				position -= 1

if __name__=="__main__":
	fP = flipPancake()
	testCases = 1
	with open('/Users/saavn/Downloads/A-large.in.txt','rb') as fptr:
		fptr.next()
		for row in fptr:
			fP.stringArray = []
			case = row.split(' ')
			fP.flipperSize = int(case[1])
			for i in case[0]:
				fP.stringArray.append(i)
			fP.startProcessing(testCases)
			testCases +=1