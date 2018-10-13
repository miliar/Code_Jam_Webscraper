class LawnMower:
	lawns = []
	
	def __init__(self, lawns):
		self.lawns = lawns
		for i, lawn in enumerate(lawns):
			print 'Case #%d:' % (i+1),
			if self.isValidLawn(lawn):
				print 'YES'
			else:
				print 'NO'
	
	def isValidLawn(self, lawn):
		for i in range(len(lawn)):
			for j in range(len(lawn[0])):
				if not self.isValid(lawn, i, j):
					return False
		return True
	
	def isValid(self, lawn, i, j):
		return not (self.hasHigherVerticle(lawn, i, j) and self.hasHigherHorizontal(lawn, i,j))


	def hasHigherVerticle(self, lawn, i, j):
		val = lawn[i][j]
		for row in lawn:
			if row[j] > val:
				return True
		return False
	
	def hasHigherHorizontal(self, lawn, i, j):
		val = lawn[i][j]
		for height in lawn[i]:
			if height > val:
				return True
		return False

def parseInputToLawns(inputFile):
	lines = [line.strip() for line in open(inputFile)]
	lawns = []
	numLawns = int(lines[0])
	startLine = 1
	
	for i in range(numLawns):
		rows, cols = lines[startLine].split(' ')
		rows = int(rows)
		colos = int(cols)
		lawns.append(addLawn(lines[startLine+1:startLine+rows+1]))
		startLine += (rows+1)
		
	return lawns

def addLawn(lines):
	lawn = []
	for line in lines:
 		lawn.append(addRow(line))
 	return lawn
		
def addRow(line):
	row = []
	for c in line.split(' '):
		row.append(int(c))
	return row
			

lawns = parseInputToLawns('B-Large.in')

LawnMower(lawns)