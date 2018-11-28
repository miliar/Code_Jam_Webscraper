#code Chal Prob 2
from decimal import *

class Cookie():
	def __init__(self, farmCost, farmBonus, goal):
		self.goal = goal
		self.cookieRate = 2.0
		self.farmCost = farmCost
		self.farmBonus = farmBonus

	def calc_total_time(self):
		#this will calculate the total time needed to solve the problem
		waitTime = Decimal(self.goal / self.cookieRate)
		newWaitTime = Decimal(0)
		sumFarm = 0
		for i in xrange(100000):
			#try to buy a farm
			farmWait = Decimal(self.farmCost / self.cookieRate)
			newWaitTime = farmWait + Decimal(self.goal / ( self.cookieRate + self.farmBonus))
			if newWaitTime < waitTime:
				#reset the wait time.
				sumFarm += farmWait
				self.cookieRate += self.farmBonus
				waitTime = Decimal(self.goal / self.cookieRate)
			else:
				return sumFarm + waitTime

class Prob2():

	def __init__(self):
		self.numTests = 0
		#read in the file named prob2.txt
		f = open("prob2.txt", 'r')
		self.numTests = int(f.readline())
		for test in xrange(self.numTests):
			#calculate the total time for each line
			line = f.readline().split(" ")
			#print line
			cook = Cookie(float(line[0]), float(line[1]), float(line[2]))
			time = cook.calc_total_time()
			self.output(test, time)

	def output(self, testNum, totalTime):
		f = open("results.txt", 'a')
		s = "Case #" + str(testNum+1) + ": " + '{0:.25}'.format(totalTime) + "\n"
		f.write(s)



prob2 = Prob2()
