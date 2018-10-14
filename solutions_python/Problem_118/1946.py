import re, operator, gcj, math, copy

inputfile = "C-small-attempt0.in"
out = gcj.Output("C-small-attempt0.out")
inputfile = open(inputfile, "r")
firstline = inputfile.next()
nrCases = int(firstline)
print nrCases

class Palin():
	def __init__(self, A, B):
		self.sA = int(math.ceil(math.sqrt(A*1.0)))
		self.sB = int(math.floor(math.sqrt(B*1.0)))
		
	def solve(self):
		count = 0
		for i in range(self.sA, self.sB+1):
			if self.ispalindrome(i) and self.ispalindrome(int(math.pow(i,2))):
				count+=1
				print i
		return count

	def ispalindrome(self, num):
		x = str(num)
		y = copy.deepcopy(x)
		y = y[::-1]
		return x==y
		

#start cases
i = 1
stop = False
while i<nrCases+1 and not stop:
	line = inputfile.next()
	line = line[:-1]
	line = re.split("\s", line)
	A = int(line[0])
	B = int(line[1])
	p = Palin(A,B)
	out.writeNext(p.solve())
	i+=1
