class Tree:
	def __init__(self):
		self._fet = ""
		self._weg = 1.0
		self._left = None
		self._right = None
	def setFet(self,ofet):
		self._fet = ofet
	def setWeg(self,oweg):
		self._weg = oweg
	def setLeft(self,oleft):
		self._left = oleft
	def setRight(self,oright):
		self._right = oright
	def leaf(self):
		return self._left == None and self._right == None
	def printTree(self):
		if self != None:
			print str(self._weg) + "   " + str(self._fet)
			if not self.leaf():
				self._left.printTree()
				self._right.printTree()
		
	

def buildTree(file):
	me = Tree()
	line = ""
	while(line==""):
		line = file.readline().strip()
		line = line.replace(')','').strip()
		line = line.replace('(','').strip()
	
	temp = line.split(" ")
	if len(temp) == 1:
		me.setWeg(float(line))
		return me
	temp[0] = float(temp[0])
	me.setWeg(temp[0])
	me.setFet(temp[1])
	me.setLeft(buildTree(file))
	me.setRight(buildTree(file))
	return me
		
def getResult(tree, data):
	if tree.leaf():
		return tree._weg
	if data == None:
		return tree._weg * getResult(tree._right, data)
	if data.__contains__(tree._fet):
		return tree._weg * getResult(tree._left, data)
	return tree._weg * getResult(tree._right, data)
		
		
def getRes(tree, animal):
	data = animal.split(" ")
	if len(data) <= 2:
		return getResult(tree,None)
	return getResult(tree, data[2:])

	
	
	
	
#print getResult("561")
#print getRes("982561")
	
file = open("c:\input.txt")
params = int(file.readline().strip())
for i in range(1,params+1):
	line = ""
	while(line==""):
		line = file.readline().strip()
		line = line.replace(')','').strip()
		line = line.replace('(','').strip()
	line = int(line)
	tree = buildTree(file)
	print "Case #"+str(i) + ":"
	line = ""
	while(line==""):
		line = file.readline().strip()
		line = line.replace(')','').strip()
		line = line.replace('(','').strip()
	line = int(line)
	for j in range(0,line):
		check = ""
		while(check==""):
			check = file.readline().strip()
			check = check.replace(')','').strip()
			check = check.replace('(','').strip()
		res = getRes(tree, check)
		print "%.7f"%res
