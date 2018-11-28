import math
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

def calc(R, T):
	N = float((-2*R+1+math.sqrt(float(4*R*R-4*R+1+8*T)))) / 4

	return int(N)

r.open("A-small-attempt0.in", "A-small-attempt0.out")
for i in range(0, r.getCases()):
	a = r.readLine(" ")

	R = int(a[0])
	T = int(a[1])

	r.out(str(calc(R, T)))

r.close()
