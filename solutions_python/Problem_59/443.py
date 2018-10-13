import sys

class Tree:
	children = {}
		
	def __init__(self):
		self.children = {}
	def create(self, new):
		if (new == []):
			return
		else:
			top = new[0].strip()
			relative = new[1:]
			if (top in self.children):
				self.children[top].create(relative)
			else:
				self.children[top] = Tree()
				self.children[top].create(relative)
	def count(self):
		childCount = 0
		if (len(self.children) == 0):
			return 0
		else:
			for eachChild in self.children:
				childCount = childCount + self.children[eachChild].count()
			return len(self.children) + childCount
	def printd(self):
		for x in self.children:
			print x
			self.children[x].printd()

						
filename = sys.argv[1]
inputFile = open(filename, "r")
lines = inputFile.readlines()
cases = int(lines[0])

index = 1
for i in range(1,cases+1):
	params = lines[index].split()
	existing = int(params[0])
	toCreate = int(params[1])
	index = index + 1
	
	dirTree = Tree()
	#print "Existing"
	for j in range(existing):
		#print "Creating",lines[index].split("/")[1:]
		dirTree.create(lines[index].split("/")[1:])
		index = index + 1
	counts = dirTree.count()
	#print "Counts", counts
	
	for k in range(toCreate):
		#print "Creating",lines[index].split("/")[1:]
		dirTree.create(lines[index].split("/")[1:])
		index = index + 1
	#print "Final Counts", dirTree.count()
	#dirTree.printd()
	print "Case #" + str(i) + ":", (dirTree.count() - counts)
	
		
