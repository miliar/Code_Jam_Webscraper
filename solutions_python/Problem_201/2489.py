import sys

class BathroomStall:
	def __init__(self, isOccupied, leftUnoccupied=None, rightUnoccupied=None, stallLeft=None, stallRight=None):
		self.isOccupied = isOccupied
		self.leftUnoccupied = leftUnoccupied
		self.rightUnoccupied = rightUnoccupied
		self.stallLeft = stallLeft
		self.stallRight = stallRight
	def __str__(self):
		return str([self.isOccupied, self.leftUnoccupied, self.rightUnoccupied, self.stallLeft, self.stallRight])
	def findLeftUnoccupied(self):
		#print self.stallLeft
		if self.stallLeft.isOccupied:
			self.leftUnoccupied = 0
			#print "left stall is occupied"
		else:
			self.leftUnoccupied = self.stallLeft.leftUnoccupied + 1
	def findRightUnoccupied(self):
		if self.stallRight.isOccupied:
			self.rightUnoccupied = 0
			#print "right stall is occupied"
		else:
			self.rightUnoccupied = self.stallRight.rightUnoccupied + 1 
	def addStallLeft(self, stallLeft):
		self.stallLeft = stallLeft	
	def addStallRight(self, stallRight):
		self.stallRight = stallRight
	def findMinLR(self):
		self.minLR = min(self.leftUnoccupied, self.rightUnoccupied)
		return min(self.leftUnoccupied, self.rightUnoccupied)
	def findMaxLR(self):
		self.maxLR = max(self.leftUnoccupied, self.rightUnoccupied)
		return max(self.leftUnoccupied, self.rightUnoccupied)

def initializeBathroomStalls(N):
	
	bathroomStalls = [BathroomStall(1)] 
	for i in range(0, N):
		bathroomStalls += [BathroomStall(0)]
	bathroomStalls += [BathroomStall(1)]
	#print bathroomStalls
	#for bathroomStall in bathroomStalls:
		#print "bathroom stall"
		#print bathroomStall
	for i in range(1, len(bathroomStalls)-1):
		bathroomStalls[i].addStallLeft(bathroomStalls[i-1])
		bathroomStalls[i].addStallRight(bathroomStalls[i+1])      
	for i in range(1, len(bathroomStalls)-1):
		bathroomStalls[i].findLeftUnoccupied()
	for i in range(len(bathroomStalls)-2, 0, -1):
		bathroomStalls[i].findRightUnoccupied()
	for i in range(1, len(bathroomStalls)-1):
		bathroomStalls[i].findMinLR()
		bathroomStalls[i].findMaxLR()
	#print bathroomStalls
	#for bathroomStall in bathroomStalls:
		#print "bathroom stall"
		#print bathroomStall
	return bathroomStalls

def findStall(currency):
	#[[l,r], [l,r]]
	#find the maximal min
	maximal_min = 0
	maximal_mins = []
	for i in range(0, len(currency)):
		if currency[i].minLR > maximal_min and not currency[i].isOccupied:
			maximal_min = currency[i].minLR
	for i in range(0, len(currency)):
		if currency[i].minLR == maximal_min and not currency[i].isOccupied:
			maximal_mins += [i] 
	#print "list of maximal_mins " + str(maximal_mins)
	maximal_max = 0
	maximal_maxs = []
	if len(maximal_mins) > 1:
	#find the maximal max
		for i in maximal_mins:
			if currency[i].maxLR > maximal_max and not currency[i].isOccupied:
				maximal_max = currency[i].maxLR
		for i in maximal_mins:
			if currency[i].maxLR == maximal_max and not currency[i].isOccupied:
				maximal_maxs += [i]
		#print "list of maximal_maxs " + str(maximal_maxs)
		return maximal_maxs[0]+1
	else:	
		#print "returning maximal_mins"
		return maximal_mins[0]+1
	
def updateBathroomStalls(bathroomStalls, justchanged):
	for i in range(justchanged-1, 0, -1):
		if bathroomStalls[i].isOccupied:
			break
		bathroomStalls[i].findRightUnoccupied()
	for i in range(justchanged+1, len(bathroomStalls)-1, 1):
		if bathroomStalls[i].isOccupied:
			break
		bathroomStalls[i].findLeftUnoccupied()
	for i in range(1, len(bathroomStalls)-1):
		bathroomStalls[i].findMinLR()
		bathroomStalls[i].findMaxLR()
	return
	
def printBathroomStalls(brs, verbose=False):
	if verbose:
		for br in brs:
			print br
	else:
		printer = []
		for br in brs:
			printer += [br.isOccupied]
		#print printer

f = open(sys.argv[1])

lines = f.readlines()

f.close()

T = int(lines[0])

p = open(sys.argv[2], "w")

for t in range(1, T+1):
	N = int(lines[t].split(" ")[0])
	K = int(lines[t].split(" ")[1])
	#print "Case " + str(t) + " N=" + str(N) + " K=" + str(K)
	bathroomStalls = initializeBathroomStalls(N)
	#print "in the beginning: "
	printBathroomStalls(bathroomStalls)
	current = [[x.findMinLR(), x.findMaxLR()] for x in bathroomStalls]
	#print "list of [minlr, maxlr] " + str(current)
	#mins = [x[0] for x in current]
	#maxs = [x[1] for x in current]
	for i in range(0, K-1):
		stall = findStall(bathroomStalls[1:-1])
		bathroomStalls[stall].isOccupied = 1
		updateBathroomStalls(bathroomStalls, stall)
		current = [[x.findMinLR(), x.findMaxLR()] for x in bathroomStalls]
		#print "after person: " + str(i + 1)
		printBathroomStalls(bathroomStalls)
		#print "list of [minlr, maxlr] " + str(current)
		
	#final person
	stall = findStall(bathroomStalls[1:-1])
	y = bathroomStalls[stall].maxLR
	z = bathroomStalls[stall].minLR
	#print bathroom stalls
	#print "at the end"
	printBathroomStalls(bathroomStalls)
	p.write("Case #" + str(t) + ": " + str(y) + " " + str(z) + "\n")
	#print "Case #" + str(t) + ": " + str(y) + " " + str(z)

p.close()
	
