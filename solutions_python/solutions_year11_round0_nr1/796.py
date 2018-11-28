#!/usr/bin/python
class Color():
	def __init__(self, name, curPriority, actionlist):
		self.name = name
		self.position = 1
		self.done = False
		self.curDest = 0
		self.priority = curPriority
		self.actionlist = actionlist
		self.pushButton()
	def setCurDest(self, number):
		self.curDest = number
	def getFutureStep(self):
		if (self.position > self.curDest):
			return self.position - 1
		elif (self.position < self.curDest):
			return self.position + 1
		else:
			return self.curDest
	def isReadyButton(self):
		if (self.position == self.curDest):
			return True
		else:
			return False
	def walk(self):
		self.position = self.getFutureStep()
	def pushButton(self):
		if (len(self.actionlist) != 0):
			self.curDest = self.actionlist[0]
			self.actionlist.pop(0)
		else:
			self.done = True
			
					
def main():
	numberOfCases = int(raw_input())
	results = list()
	if (numberOfCases):
		for case in range(1,numberOfCases+1):
	#		currentTime = 0
	#		key = 0
	#		numSecondsNeeded = 0
			testString = raw_input().split(" ")
			buttonsPressed = int(testString[0])
			testString.pop(0)
			results.append( doWork(case, buttonsPressed, testString) )
		casenumber = 1
		for each in results:
			printWork(casenumber, each)
			casenumber += 1									
			
#def moveColor(color, amount):
def doWork(numCase, numActions, termArray):
	curPri = 0
	if( numActions == 1 ):
		numSeconds = termArray[1]
		return numSeconds
	else:
		orangearray = list()
		bluearray = list()
		totalarray = list()
	 	#make arrays, orange, blue, total
		while (len(termArray) != 0):
				if (termArray[0] == "O"):
					orangearray.append(int(termArray[1]))
				else:
					bluearray.append(int(termArray[1]))				
				totalarray.append(termArray[0])
				termArray.pop(0)
				termArray.pop(0)
		
		robotOrange = Color(name="O", curPriority=curPri, actionlist=orangearray)
		robotBlue = Color(name="B", curPriority=curPri, actionlist=bluearray)
		numSeconds = 0
		while (True):
			if ( (robotOrange.done == True) and (robotBlue.done == True) ):
				return numSeconds
		#	print "totalarray[0]=" + str(totalarray[0])

			if (totalarray[0] == "O"):
				if (robotOrange.isReadyButton() == True):
					robotOrange.pushButton()
					totalarray.pop(0)
				else:
					robotOrange.walk()
				robotBlue.walk()
			elif (totalarray[0] == "B"):
				if (robotBlue.isReadyButton() == True):
					robotBlue.pushButton()
					totalarray.pop(0)
				else:
					robotBlue.walk()
				robotOrange.walk()
			numSeconds += 1	
					
				 

def printWork(numCase, numSeconds):
	print "Case #" + str(numCase) + ": " + str(numSeconds)

main()
