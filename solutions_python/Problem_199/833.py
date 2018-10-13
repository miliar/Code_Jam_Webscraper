class Case(object):
	def __init__(self, k, l):
		self.l = l
		self.k = k
		self.size = len(l)
		self.flips = 0

	def flip(self, i):
		for j in range(self.k):
			if self.l[i + j] == '+':
				self.l[i + j] = '-'
			elif self.l[i + j] == '-':
				self.l[i + j] = '+'

	def check(self):
		res = True
		for j in range(1, self.k):
			if self.l[-j] == '-':
				res = False
		return res

	def do(self):
		for i in range(self.size - self.k + 1):
			if self.l[i] == '-':
				self.flip(i)
				self.flips += 1

		if self.check():
			return str(self.flips)
		else:
			return "IMPOSSIBLE"




infile = open("input_file.txt", 'r')
outfile = open("output_file.txt", 'w')

T = int(infile.readline())
for i in range(T):
	inStr = infile.readline().split()
	k = int(inStr[1])
	l = list(inStr[0])
	c = Case(k, l)
	outfile.write("Case #" + str(i + 1) + ": " + c.do() + "\n")

