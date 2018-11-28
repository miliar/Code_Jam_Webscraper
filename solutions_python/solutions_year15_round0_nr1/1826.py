OUTPATH = "out.txt"
def loadCases (filePath):
	data = []
	nCases = 0
	with open (filePath, 'r') as file:
		fileData = file.read()
		data = fileData.split("\n")
		nCases = data.pop(0)
		data.pop()
	return (nCases, data)
	
def getNumFriends (nCases, data):
	nCase = 0
	clearfile()
	while data:
		nCase += 1
		currentCase = data.pop(0)
		currentCase = currentCase.split(" ")
		ShyMax = int(currentCase[0])
		audience = currentCase[1]
		peopleStand = 0
		friendsNeed = 0
		ShyLvl = 0
		#print (currentCase)
		while audience:
			peopleLvl = int(audience[0])
			audience = audience[1:]
			if peopleLvl > 0:
				if (peopleStand+friendsNeed) < ShyLvl:
					friendsNeed = ShyLvl - peopleStand
			#print (friendsNeed, ShyLvl, peopleLvl, peopleStand)
			peopleStand += peopleLvl
			ShyLvl += 1
		#print("case end ------------")
		writeOutput(nCase, friendsNeed)

def clearfile ():
	with open (OUTPATH, 'w') as file:
			file.write("")
		
def writeOutput (nCase, friendsNeed):
	with open (OUTPATH, 'a') as file:
		file.write ("Case #%i: %i\n" % (nCase, friendsNeed) )
		
if __name__ == "__main__":
	nCases, data =loadCases("A-large.in")
	getNumFriends (nCases, data)