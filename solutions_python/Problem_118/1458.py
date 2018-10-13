class FairAndSquare:
	tests = []
	fairAndSquares = {}
	
	def __init__(self, tests):
		self.tests = tests
		for i, test in enumerate(tests):
			print 'Case #%d: %d' % (i+1, self.calculateFairAndSquare(test))
		
	def calculateFairAndSquare(self, test):
		counter = 0
		i = test[0]
		while i <= test[1]:
			if self.isFairAndSquare(i):
				#print 'num: %d' % i
				counter+=1
			i+=1
		return counter

	def isFairAndSquare(self, i):
		import math
		root = math.sqrt(i)
		#print 'sqrt: ' + str(root)
		return isFair(i) and isInteger(root) and isFair(int(root))
			
def isFair(i):
	s = str(i)
	while len(s) > 0:
		start = s[0]
		end = s[-1]
		s = s[1:]
		s = s[:-1]
		if start != end:
			#print 'No: ' + str(start) + ' ' + end
			return False
	#print str(i) + ' is fair'
	return True

def isInteger(root):
	return root - int(root) == 0

def parseInput(inputFile):
	lines = [line.strip() for line in open(inputFile)]
	tests = []
	num = int(lines[0])
	startLine = 1
	
	for i in range(num):
		line = lines[i+1]
		vals = line.split(' ')
		start = long(vals[0])
		end = long(vals[1])
		tests.append((start,end))
	#print tests
	return tests

tests = parseInput('C-small-attempt0.in')

FairAndSquare(tests)