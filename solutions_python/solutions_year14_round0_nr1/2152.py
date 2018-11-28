import os, sys, time

class Problem(object):
	def __init__(self, baseFilename):
		self.inFilename = baseFilename + '.in'
		self.outFilename = baseFilename + '.out'
	
		self.f_in = open(self.inFilename, 'r')
		self.f_out = open(self.outFilename, 'w')

		self.numberOfTestCases = None # read this from the file
		self.caseNumber = 0;
		
		self.badMagicianString = 'Bad magician!'
		self.volunteerCheatedString = 'Volunteer cheated!'
		
	def getHeader(self):
		line = self.f_in.readline().strip()
		self.numberOfTestCases = int(line)
		print 'Number of Test Cases: %d' % self.numberOfTestCases
				
	def getProblem(self):
		self.caseNumber += 1 # increment when read problem

		self.answer = {}
		self.cards = {}
		
		for h in ['A', 'B']:
			self.answer[h] = int(self.f_in.readline().strip())-1 # handle zero-base here
			self.cards[h] = []
			for i in range(4):
				line = self.f_in.readline().strip()
				cardRow = [int(c) for c in line.split(' ')]
				self.cards[h].append(cardRow)
			
		# now we have two answers and two sets of cards
		# self.answer
		# self.cards
		
		# note: cards in the same row are self.cards['A'][0] (for example)
		# note: rows are from 0-3, inclusive
		
	def compute(self):
		possibleCards = {}
		# determine possible cards based on first answer
		for h in ['A', 'B']:
			possibleCards[h] = self.cards[h][ self.answer[h] ]
				
#		print possibleCards
		
		# now look for how many cards in A are in B
		solutions = []
		for c in possibleCards['A']:
			if c in possibleCards['B']:
				solutions.append(c)
		
		count = len(solutions)
		
		if count == 1: # the card is found since only one in common
			self.answer = '%d' % solutions[0]
		elif count == 0: # volunteer cheated since no cards in common
			self.answer = self.volunteerCheatedString
		else: 
			self.answer = self.badMagicianString # since more than one answe is posible
			                                     # based on the shuffle
				
	def writeAnswer(self):
		s = 'Case #%d: %s' % (self.caseNumber, self.answer)
		self.f_out.write(s + '\n')
		
	def solve(self):
		self.getHeader()
		for i in xrange(self.numberOfTestCases):
			self.getProblem()
			
			print 'Solving: %d' % self.caseNumber
			
			start = time.time()
			self.compute()
			elapsedTime = time.time() - start
			
			print '\tSolved %d in %f seconds' % (self.caseNumber, elapsedTime)
			
			self.writeAnswer()

p = Problem(baseFilename = 'A-small-attempt0')
p.solve()
