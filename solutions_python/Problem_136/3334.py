'''
Created on Apr 11, 2014

@author: Mike
'''

class TestCase:
	
	def __init__(self, c, f, x):
		self.c = c
		self.f = f
		self.x = x
		self.currentRate = 2
		self.cookies = 0
		self.time = 0.0
		self.timeslice = 0.00001
		
	def getTime(self):
		run = True
	
		while run :
			
			self.time += self.timeToNextFarm()
			self.cookies += self.currentRate * self.timeToNextFarm()
			
			minimumToGoal = min(self.timeToGoalWithFarm(), self.timeToGoalWithoutFarm())
			if(minimumToGoal < self.timeToNextFarm()) :
				self.time += minimumToGoal
				break
			if(self.timeToGoalWithFarm() < self.timeToGoalWithoutFarm()) :
				self.currentRate += self.f
				self.cookies -= self.c
				
			
			
				
		return self.time
					
		
	def buyAnother(self):
		return (self.timeToGoalWithFarm() < self.timeToGoalWithoutFarm())
	
	def timeToNextFarm(self):
		return self.c / self.currentRate
	
	def timeToGoalWithFarm(self):
		return (self.x - (self.cookies - self.c)) / (self.currentRate + self.f)
	
	def timeToGoalWithoutFarm(self):
		return (self.x - self.cookies) / self.currentRate


def readCases():
	f = open('B-small-attempt1.in', 'r')
	caseCount = int(f.readline())
	cases = []
	for i in range(0,caseCount)  :
		vals = [float(x) for x in f.readline().split(' ')]
		cases.append(TestCase(vals[0], vals[1], vals[2]))
		
	return cases

def main():
	cases = readCases()
	i = 1
	for case in cases :
		print "Case #" + str(i) + ": " + str(case.getTime())
		i += 1
	pass

if __name__ == '__main__':
	main()
	pass