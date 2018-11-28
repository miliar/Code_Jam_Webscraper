import re, operator, gcj

inputfile = "B-small-attempt0.in"
out = gcj.Output("B-small-attempt0.out")
inputfile = open(inputfile, "r")
firstline = inputfile.next()
nrCases = int(firstline)
print nrCases

class Gazon():
	def __init__(self, N,M, lines):
		pass #parse
		print "NEW GAZON:"
		print "N: %d"%N
		print "M: %d"%M
		self.N = N
		self.M = M
		self.rows = []
		for line in lines:
			row = re.split("\s",line)
			self.rows.append(row)
		for row in self.rows:
			print row
		self.columns = []
		i = 0
		while i<self.M:
			column = []
			for row in self.rows:
				column.append(row[i])
			self.columns.append(column)
			i += 1
		for column in self.columns:
			#print column
			pass

	def solve(self):
		for i in range(0,self.N):
			for j in range(0,self.M):
				vert = self.checkVertical(i,j)
				hori = self.checkHorizontal(i,j)
				if not(vert or hori):
					return "NO"
		return "YES"

	def checkVertical(self, i, j):
		pass
		level = self.rows[i][j]
		row = self.rows[i]
		for el in row:
			if el>level:
				return False
		return True

	def checkHorizontal(self, i, j):
		level = self.rows[i][j]
		column = self.columns[j]
		for el in column:
			if el>level:
				return False
		return True

#start cases
i = 1
stop = False
while i<nrCases+1 and not stop:
	setline = inputfile.next()
	print setline
	setline = setline[:-1]
	setline = re.split("\s",setline)
	N = int(setline[0])
	M = int(setline[1])
	print (N,M)
	j = 0
	jstop = False
	lines = []
	while j<N and not jstop:
		line = inputfile.next()
		line = line[:-1]
		lines.append(line)
		j+=1
	i+=1
	g = Gazon(N,M,lines)
	out.writeNext(g.solve())

