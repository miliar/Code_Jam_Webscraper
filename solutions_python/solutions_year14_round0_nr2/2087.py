import os, sys, time

FACTOR = 1e9

class Problem(object):
	def __init__(self, baseFilename):
		self.inFilename = baseFilename + '.in'
		self.outFilename = baseFilename + '.out'
	
		self.f_in = open(self.inFilename, 'r')
		self.f_out = open(self.outFilename, 'w')

		self.numberOfTestCases = None # read this from the file
		self.caseNumber = 0;
		
		
	def getHeader(self):
		# get T
		line = self.f_in.readline().strip()
		self.numberOfTestCases = int(line)
		print 'Number of Test Cases: %d' % self.numberOfTestCases
				
	def getProblem(self):
		self.caseNumber += 1 # increment when read problem

		line = self.f_in.readline().strip()
		
		# should be able to get 10^-6 precision with a regular float
		# provided there are not too many small additions in the problem
		
		# convert to fixed point
		(self.C, self.F, self.X) = [float(v) for v in line.split(' ')]

		# do integer arithmetic
		self.C = int(self.C * FACTOR)
		self.X = int(self.X * FACTOR)
		self.F = int(self.F * FACTOR)
		
	def compute(self):
		# each game starts 0 cookies
		# at the start of the came, we gain cookies at 2 per second in continuous time
		
		# INPUT
		# self.C is the cost of the cookie farm
		# self.F is the number of cookies per second per farm
		# self.X is the goal amount (not including what was spent on farms)
		
		# OUTPUT
		# self.t is the minimum time to reach the goal
		
		# STRATEGY
		# save cookies and compute how long at the current rate until we reach goal
		# if buying another cookie farm gets us there faster, then buy it, otherwise
		# just wait it out.
		
		self.cookies = 0.0
		self.rate = int(2 * FACTOR)
		self.timeElapsed = 0.0
		
		done = False
		while not done:
			timeAtPresentRateToGoal = self.timeToGoal(self.cookies, self.rate, self.X)
			
			timeUntilAffordNextFarm = self.timeToGoal(self.cookies, self.rate, self.C)
			
			# assume we buy another farm as soon as we can.
			#   we will have 0 cookies after doing so, but the cookie rate is increased
			timeAfterBuyingNextFarmToGoal = timeUntilAffordNextFarm + self.timeToGoal(0, 
			                                                                          self.rate + self.F, 
																											  self.X)

			# go with whichever solution is shorter
			if timeAfterBuyingNextFarmToGoal < timeAtPresentRateToGoal:
				self.timeElapsed += timeUntilAffordNextFarm
				self.rate += self.F
				self.cookies = 0
			else: # always end on this case
				self.timeElapsed += timeAtPresentRateToGoal
				done = True
			
			# output a 7-digit float
			self.answer = '%.7f' % (self.timeElapsed / FACTOR)
		
	def timeToGoal(self, cookies, rate, goal):
			t = int(round((goal - cookies) / float(rate) * FACTOR, 0))
		
			return t
	
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

p = Problem(baseFilename = 'B-large')
p.solve()
