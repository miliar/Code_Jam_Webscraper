class CookieProduct:
	def __init__(self):
		self.farmProduct = 0.0
		self.farmCost = 0.0
		self.goal = 0.0
		self.totalTime = 0.0;
		self.cookiePersec = 2.0;
		self.caseNumber = 1;
		self.text = '';

	def setFarmProduct(self, farmProduct):
		self.farmProduct = float(farmProduct)

	def setFarmCost(self, farmCost):
		self.farmCost = float(farmCost)

	def setGoal(self, goal):
		self.goal = float(goal)

	def produce(self):
		while(self.producePredict()): pass
		self.text = self.text+('Case #%d: %lf\n'%(self.caseNumber, self.totalTime))

	def producePredict(self):
		goalNow = self.timeToGoal()
		timeBuy = self.timeToBuy()
		if(goalNow > (timeBuy+self.timeNewFarm())):
			self.cookiePersec = self.cookiePersec+self.farmProduct
			self.totalTime = self.totalTime + timeBuy
			return True
		else: 
			self.totalTime = self.totalTime + goalNow
			return False

	def timeToGoal(self):
		return self.goal/self.cookiePersec

	def timeToBuy(self):
		return self.farmCost/self.cookiePersec

	def timeNewFarm(self):
		return self.goal/(self.cookiePersec+self.farmProduct)

	def reset(self, caseNumber):
		self.farmProduct = 0.0
		self.farmCost = 0.0
		self.goal = 0.0
		self.totalTime = 0.0;
		self.cookiePersec = 2.0;
		self.caseNumber = caseNumber;

if __name__ == "__main__" :
	cookie = CookieProduct()
	with open('B-large.in', 'r') as testCaseFile:
		totalTestCase = int(testCaseFile.readline())
		for testCase in range(totalTestCase):
			case = testCaseFile.readline()
			farmCost, farmProduct, goal = case.split(' ', 3)
			goal = goal[:-1]

			cookie.setFarmCost(farmCost)
			cookie.setFarmProduct(farmProduct)
			cookie.setGoal(goal)
			cookie.produce()
			cookie.reset(testCase+2)
	with open('CookieProduct.out', 'w+') as outPut:
		outPut.write(cookie.text)
