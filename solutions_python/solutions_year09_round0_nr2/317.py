class BasinMap:
	def __init__(self, height, width, mapstring):
		self.height = height
		self.width = width
		self.alt = []	# 2d array, altitudes
		self.basin = {}	# sink(x,y) => basin cell(x,y) list
		self.sinks = []	# 2d array, holds (x,y) of sink
	
		#self.highest = 0
		for i in range(height):
			self.alt.append( [] )
			line = mapstring[i].split(' ')
			for j in range(width):
				n = int(line[j])
				self.alt[i].append(n)
				#if (self.highest < n)
				#	self.highest = n
		#self.highest += 1

		for i in range(height):
			self.sinks.append( [] )
			for j in range(width):
				self.sinks[i].append( None )

	def getSink(self, r, c):	# row, column
		if self.sinks[r][c] != None:
			return self.sinks[r][c]

		lowest = self.alt[r][c]
		sinkr, sinkc = r, c

		if 0 < r and self.alt[r-1][c] < lowest:
			lowest = self.alt[r-1][c]
			sinkr, sinkc = r-1, c

		if 0 < c and self.alt[r][c-1] < lowest:
			lowest = self.alt[r][c-1]
			sinkr, sinkc = r, c-1

		if c + 1 < self.width and self.alt[r][c+1] < lowest:
			lowest = self.alt[r][c+1]
			sinkr, sinkc = r, c+1

		if r + 1 < self.height and self.alt[r+1][c] < lowest:
			lowest = self.alt[r+1][c]
			sinkr, sinkc = r+1, c

		if sinkr == r and sinkc == c:
			self.sinks[r][c] = (r, c)
			self.basin[(r,c)] = [(r,c)]
			return (r, c)
		else:
			s = self.getSink(sinkr, sinkc)
			self.sinks[r][c] = s
			self.basin[s].append( (r, c) )
			return s

	def getLabel(self):
		for i in range(self.height):
			for j in range(self.width):
				self.getSink(i, j)

		label = []
		for i in range(self.height):
			label.append([])
			for j in range(self.width):
				label[i].append([])

		# lowest cell ==> cell list
		basin2 = {}
		for cells in self.basin.values():
			cells.sort()
			basin2[cells[0]] = cells

		lblstr = "abcdefghijklmnopqrstuvwxyz"
		idx = 0
		keys = basin2.keys()
		keys.sort()
		for key in keys:
			for cell in basin2[key]:
				label[cell[0]][cell[1]] = lblstr[idx]
			idx += 1

		return label


import sys

fileNameIn = sys.argv[1]
if fileNameIn[-3:] != ".in":
	print "extension is not 'in'"
	sys.exit()
fileNameOut = fileNameIn[0:-3] + ".out"
print fileNameOut

fileIn = open(fileNameIn, 'r')
fileOut = open(fileNameOut, 'w')


lines = fileIn.readlines()
idx = 0

mapcnt = int(lines[idx])
idx += 1

for i in range(mapcnt):
	line = lines[idx].split(' ')
	idx += 1
	height = int(line[0])
	width = int(line[1])

	fileOut.write("Case #{0}:\n".format(i+1))
	basinmap = BasinMap(height, width, lines[idx : idx+height])

	for row in basinmap.getLabel():
		for cell in row:
			fileOut.write("{0} ".format(cell))
		fileOut.write("\n")

	idx += height

