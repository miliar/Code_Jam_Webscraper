debug = True

class main():
	
	beforeStart = 0
	beforeEnd = 0
	
	cycleStart = 0
	cycleEnd = 0
	
	afterStart = 0
	afterEnd = 0
	
	def printCycleData(self):
		print '\n==== cycle data ================='
		print 'Data beforeStartIndex: ' + str(self.beforeStartIndex)
		print 'Data beforeNrOfRides: ' + str(self.beforeNrOfRides )
		
		#the first caught cycle (could be that there is no cycle)
		print 'Data cycleStartIndex: ' +str(self.cycleStartIndex)
		print 'Data fullCycleRuns: ' +str(self.fullCycleRuns)
		print 'Data ridesPerCycle: ' +str(self.ridesPerCycle)
		
		
		print 'Data afterStartIndex: ' +str(self.afterStartIndex )
		print 'Data afterNrOfRides: ' +str(self.afterNrOfRides )
	
	def resetCycleData(self):
		#the index to begin/end at for before-part
		self.beforeStartIndex = 0
		self.beforeNrOfRides = 0
		
		#the first caught cycle (could be that there is no cycle)
		self.cycleStartIndex = 0
		self.ridesPerCycle = 0
		self.fullCycleRuns = 0
		
		
		self.afterStartIndex = 0
		self.afterNrOfRides = 0
	
	def calculateCycleParams(self):
		x = 0 
		startIndexes = []
		nextId = 0
		ridingPeople = 0
		
		foundCycleOnRideNr = 0
		
		findLast = False
		firstCycleFindRide = 0
		cycleFound = False
		
		for rideNr in range(0, self.nrOfRides):
			groupNrOnThisRide = 0
			
			if(findLast == True):
				#print 'NEXT ID: ' + str( nextId)
				
				
				remainingRidesWhenFirstLoopBegins = self.nrOfRides - self.beforeNrOfRides
				
				self.fullCycleRuns = int( remainingRidesWhenFirstLoopBegins / self.ridesPerCycle)
				
				self.afterNrOfRides =  self.nrOfRides - self.beforeNrOfRides - self.ridesPerCycle*self.fullCycleRuns
				return
			
			#print '================= NEW RIDE ============'
			
			while True:
				#print 'ride Nr: ' + str(rideNr)
				
				if(groupNrOnThisRide == 0 and cycleFound == True and nextId == self.cycleStartIndex):
					self.ridesPerCycle = rideNr - foundCycleOnRideNr
					findLast = True
					self.afterStartIndex = nextId
					#print 'NEXT ID WHEN LOOP FOUND SECOND TIME: ' + str(nextId)
					self.beforeNrOfRides = foundCycleOnRideNr - self.ridesPerCycle
					
				
				if(groupNrOnThisRide == 0 and  cycleFound == False and startIndexes.count(nextId) > 0):
					cycleFound = True
					firstCycleFindRide = rideNr
					#print 'We found a cycle: '  + str(nextId)
					self.cycleStartIndex = nextId
					foundCycleOnRideNr = rideNr
				
				if(groupNrOnThisRide == 0):
					startIndexes.append(nextId)
					
				groupNrOnThisRide += 1
				
				#print 'next id: ' + str(nextId)
				
				nextVal = self.passengerGroups[nextId]
				
				#print 'nextVal: ' + str( nextVal)
				#print 'ridingPeople: ' + str(ridingPeople)
				#print 'self.peopleAtOnce: ' + str(self.peopleAtOnce)
				#print '======'
				
				if(nextVal + ridingPeople <= self.peopleAtOnce):
					ridingPeople += nextVal
					
					nextId += 1
					if(nextId >= self.nrOfGroups):
						nextId = 0
				else:
					#self.euros += ridingPeople
					ridingPeople = 0
					break;
					
		#print 'Nr of rides per cycle: ' + str(self.cycleNumber)
		#print 'Cycle starts at item nr: ' + str(self.cycleStartIndex)
	
	def getEurosForRides(self, fromIndex, nrOfRides):
		#print 'Got fromIndex: ' + str(fromIndex)
		#print 'Got nrOfRides: ' + str(nrOfRides)
		x = 0 
		startIndexes = []
		nextId = fromIndex
		ridingPeople = 0
		euros = 0
		
		
		
		for rideNr in range(0, nrOfRides):
			
			#print 'performing ride nr: ' + str(rideNr) + '<=====================??????'
			
			while True:
				#print 'ride Nr: ' + str(rideNr)
				
				#print 'next id: ' + str(nextId)
				
				nextVal = self.passengerGroups[nextId]
				
				#print 'nextVal: ' + str( nextVal)
				#print 'ridingPeople: ' + str(ridingPeople)
				#print 'self.peopleAtOnce: ' + str(self.peopleAtOnce)
				#print '======'
				
				if(nextVal + ridingPeople <= self.peopleAtOnce):
					ridingPeople += nextVal
					
					nextId += 1
					if(nextId >= self.nrOfGroups):
						nextId = 0
				else:
					euros += ridingPeople
					ridingPeople = 0
					break;
					
		
					
		#print 'Nr of rides per cycle: ' + str(self.cycleNumber)
		#print 'Cycle starts at item nr: ' + str(self.cycleStartIndex)
		
		return euros
	
	def main(self):
		#f = open('testData.txt','r');
		f = open('C-large.in','r');
		fOut = open('result_assignment_3.txt','w')

		firstLine = f.readline()
		#print 'firstLine: ' + str(firstLine)

		caseNr = 1

		while True:# in range (0, sum([1 for line in f]) -1 ):
			params = f.readline()[0:-1]
			queue = f.readline()[0:-1]
			
			if(params == '' and queue == ''):
				break;
			
			
			#set up test case parameters
			self.nrOfRides = int(params.split(" ")[0]);
			self.peopleAtOnce = int(params.split(" ")[1]);
			
			self.passengerGroups = []
			for group in queue.split(" "):
				self.passengerGroups.append(int(group))
			
			#start counting money
			self.euros = 0
			
			self.nrOfGroups = len(self.passengerGroups)
			
			self.totNrOfPeople = sum(self.passengerGroups)
			
			if( self.totNrOfPeople <= self.peopleAtOnce):
				self.euros = self.totNrOfPeople * self.nrOfRides
			else:
				#identify a cycle (start stop index)
				self.resetCycleData()
				
				#self.printCycleData()
			
				#start calculating and see if we find a cycle
				self.calculateCycleParams()
				self.printCycleData()
			
				if(self.ridesPerCycle == 0 or self.fullCycleRuns == 0):
					self.euros += self.getEurosForRides(0, self.nrOfRides)
				else:
					# calculate first part earnings
					#print 'before euros:  ' + str(self.getEurosForRides(self.beforeStartIndex, self.beforeNrOfRides))
					self.euros += self.getEurosForRides(self.beforeStartIndex, self.beforeNrOfRides)
				
					#calculate cycle earnings
					
					self.euros += self.getEurosForRides(self.cycleStartIndex, self.ridesPerCycle) * self.fullCycleRuns
					
					#calculate last part
					
					self.euros += self.getEurosForRides(self.afterStartIndex, self.afterNrOfRides)
					#print 'LAST ONE STARTS ##############################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
					#print 'after euros: ' + str(self.getEurosForRides(self.afterStartIndex, self.afterNrOfRides))
			
			print 'Case #' + str(caseNr) + ': ' + str(self.euros) + '\n'
			fOut.write('Case #' + str(caseNr) + ': ' + str(self.euros) + '\n')
			
			#print 'Params: ' + params
			#print 'Queue: ' + queue
			
			#print 'Case #' + str(caseNr) + ': ON\n'
			#fOut.write('Case #' + str(caseNr) + ': ON\n')

			caseNr += 1
			
		fOut.close()
		f.close()
		
		
m = main()
m.main()