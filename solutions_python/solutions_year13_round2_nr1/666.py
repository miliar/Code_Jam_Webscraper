class Reader:
	def __init__(self):
		self.cases = 0
		self.n = 0
	
	def open(self, inputname, outputname):
		self.input = open(inputname)
		self.output = open(outputname, 'w')
		self.cases = int(self.input.readline())
	
	def getCases(self):
		return self.cases
	
	def out(self, line):
		print 'Case #' + str(self.n + 1) + ': ' + line
		self.output.write('Case #' + str(self.n + 1) + ': ' + line + '\n')
		self.n += 1
	
	def close(self):
		self.input.close()
		self.output.close()

	def readLine(self, delimiter = None):
		if delimiter == None:
			return self.input.readline().strip()

		return self.input.readline().strip().split(delimiter)

	def readLines(self, num, delimiter = None):
		temp = []
		for i in range(0, num):
			if delimiter == None:
				temp.append(self.input.readline().strip())
			else:
				temp.append(self.input.readline().strip().split(delimiter))
		return temp

r = Reader()
r.open("A-small-attempt5.in", "A-small-attempt5.out")
#r.open("A-sample.in", "A-sample.out")

cases = r.getCases()

def solveCase():
	cucli = r.readLines(2, ' ')
	mote = int(cucli[0][0])
	others = int(cucli[0][1])
	motes = sorted([int(x) for x in cucli[1]])

	n = 0
	j = 0
	tempmote = 0
	
	for m in motes:
		if mote <= 1:
			n += 1
		else:
			if mote > m:
				mote += m
			else:
				tempmote = mote
				rounds = 0
				while tempmote <= m:
					tempmote += tempmote - 1
					rounds += 1
				if rounds < others - j:
					mote = tempmote + m
					n += rounds
				else:
					n += 1
		j += 1
	return str(n)

for i in range(0, cases):
	r.out(solveCase())

r.close()
