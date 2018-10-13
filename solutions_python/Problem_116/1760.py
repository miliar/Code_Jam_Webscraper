import re, gcj, operator

inputfile = "A-large.in"
inputfile = open(inputfile, "r")
firstline = inputfile.next()
nrCases = int(firstline)
print nrCases

class Bord():
	def __init__(self, fourlines):
		self.lines = fourlines
		self.full = ("." in reduce(operator.concat, self.lines))
		print "FULL"
		print self.full
		pass #parse
		self.rows = []
		for line in self.lines:
			row = []
			for c in line:
				if not c=="\n":
					row.append(c) 
			self.rows.append(row)
		for row in self.rows:
			#print row
			pass

		self.columns = []
		i = 0
		while i<4:
			column = []
			for row in self.rows:
				column.append(row[i])
			self.columns.append(column)
			i += 1
		for column in self.columns:
			#print column
			pass

	def solve(self):
		pass #solve
		hori = self.checkHorizontal()
		vert = self.checkVertical()
		diag = self.checkDiagonal()
		xhigh = max(hori[0], vert[0], diag[0])
		ohigh = max(hori[1], vert[1], diag[1])
		
		print hori
		print vert
		print diag
		print xhigh
		print ohigh
		if xhigh>ohigh:
			return "X won"
		if ohigh>xhigh:
			return "O won"
		if xhigh==ohigh and xhigh>0:
			return "Draw"
		if xhigh==ohigh and xhigh==0:
			if not self.full:
				return "Draw"
			else:
				return "Game has not completed"
		
	def checkHorizontal(self):
		pass
		x = False
		o = False
		for row in self.rows:
			rowstring = reduce(operator.concat, row)
			x = self.checkXWin(rowstring)if x==False or x<self.checkXWin(rowstring) else x
			o = self.checkOWin(rowstring) if o==False or o<self.checkOWin(rowstring) else o
		return (x,o)

	def checkVertical(self):
		pass
		x = False
		o = False
		status = None
		for row in self.columns:
			rowstring = reduce(operator.concat, row)
			x = self.checkXWin(rowstring)if x==False or x<self.checkXWin(rowstring) else x
			o = self.checkOWin(rowstring) if o==False or o<self.checkOWin(rowstring) else o
		return (x,o)
			

	def checkDiagonal(self):
		pass
		diagonals = []
		for o in range(-1,2):
			d=0
			diagonal = ""
			for i in range(0,4):
				while d+i < 0 or d+i+o < 0:
					d += 1
				#print "%d %d" % (i+d, i+d+o)
				if i+d>3 or i+d+o>3:
					continue
				diagonal += self.rows[d+i][d+i+o]
			diagonals.append(diagonal)
		self.rows.reverse()
		for o in range(-1,2):
			d=0
			diagonal = ""
			for i in range(0,4):
				while d+i < 0 or d+i+o < 0:
					d += 1
				#print "%d %d" % (i+d, i+d+o)
				if i+d>3 or i+d+o>3:
					continue
				diagonal += self.rows[d+i][d+i+o]
			diagonals.append(diagonal)
		#print diagonals
		x = False
		o = False
		for row in diagonals:
			rowstring = reduce(operator.concat, row)
			x = self.checkXWin(rowstring) if x==False or x<self.checkXWin(rowstring) else x
			o = self.checkOWin(rowstring) if o==False or o<self.checkOWin(rowstring) else o
		return (x,o)
		
			

	def checkXWin(self, line):
		if re.search("[XT]{4}", line):
			return 4
	#	if re.search("[XT]{3}", line):
	#		return 3
		return 0

	def checkOWin(self, line):
		if re.search("[OT]{4}", line):
			return 4
	#	if re.search("[OT]{3}", line):
	#		return 3
		return 0

out = gcj.Output("A-large.out")
#start cases
i = 1
stop = False
while i<nrCases+1 and not stop:
	print "case %d" % i
	lines = []
	j = 0
	while j<4:
		line = inputfile.next()
		lines.append(line)
		j+=1

	bord = Bord(lines)
	result = bord.solve()
	print result
	out.writeNext(result)
	try:
		spaceline = inputfile.next()
	except StopIteration:
		pass
	i+=1
