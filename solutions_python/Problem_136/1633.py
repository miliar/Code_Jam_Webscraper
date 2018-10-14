#!user/bin/python

inputpath = "cookieLargeInput.txt"


initialCookiesPerSecond=2

class CookieFarm:
	def __init__(self, farmCost, cookiesPerFarm, cookieGoal):
		self.farmCost = farmCost
		self.cookiesPerFarm = cookiesPerFarm
		self.cookieGoal = cookieGoal
		self.numberOfCookies = 0
		self.cookiesPerSecond = 2
		self.timeToGoal = 0
		self.timeAddingFarms = 0
	def runGame(self):
		self.timeToGoal = self.calculateTimeToGoal()
		notOptimized = True
		while notOptimized:
			newTimeToGoal = self.addAFarm()
			if self.timeToGoal < newTimeToGoal:
				notOptimized = False
			else:
				self.timeToGoal = newTimeToGoal
		return self.timeToGoal
	def calculateTimeForNewFarm(self):
		timeToAddFarm =  self.farmCost / self.cookiesPerSecond
		return timeToAddFarm
	def calculateTimeToGoal(self):
		return self.cookieGoal/self.cookiesPerSecond
	def addAFarm(self):		
		timeToAddFarm = self.calculateTimeForNewFarm()
		self.timeAddingFarms += timeToAddFarm
		self.cookiesPerSecond += self.cookiesPerFarm
		return self.calculateTimeToGoal() + self.timeAddingFarms

def processInput(inputpath):
	games = []
	f = open(inputpath)
	lines = f.readlines()
	numberOfGames = int(lines[0])
	for i in range(1, numberOfGames+1):
		values = lines[i].split()
		cookieFarm = CookieFarm(float(values[0]), float(values[1]), float(values[2]))
		games.append(cookieFarm)
	return games
farms = processInput(inputpath)

f = open("cookieLargeOutput.txt", "w")
for idx, farm in enumerate(farms):
	
	f.write("Case #" + str(idx+1)+": " + str(farm.runGame()) +"\n")

f.close()



