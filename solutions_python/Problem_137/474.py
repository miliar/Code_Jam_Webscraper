#!/usr/bin/env python

#from pprint import pprint

class MineSweeper:
	def __init__(self, c, r, colindex, rowindex, m):
		self.c = c
		self.r = r
		self.colindex = colindex
		self.rowindex = rowindex
		self.m = m
		self.map = {}
		self.impossible = False

	def get_output(self):
		output = ""
		if (self.impossible):
			output = "Impossible\n"
		else:
			assert self.m == 0
			#print self.m
			for i in range(self.r):
				for j in range(self.c):
					output += self.map[(i, j)]
				output += "\n"

		return output

	def sweep(self):
		rowdiff = self.r - self.rowindex
		coldiff = self.c - self.colindex
		#print "beginning---", rowdiff, coldiff, self.r, self.c, self.m
		if (self.m == 0):
			for i in range(self.rowindex, self.r):
				for j in range(self.colindex, self.c):
					if (i == (self.r - 1) and j == (self.c - 1)):
						self.map[(i, j)] = "c"
					else:
						self.map[(i, j)] = "."

		elif (rowdiff == 1):
			if (coldiff == 1): 
				self.impossible = True
			elif (coldiff > self.m):
				for i in range(self.colindex, self.colindex + self.m):
					self.map[(self.rowindex, i)] = "*"

				self.colindex += self.m
				self.m = 0
				self.sweep()

		elif (coldiff == 1):
			if (rowdiff == 1): 
				self.impossible = True
			elif (rowdiff > self.m):
				for i in range(self.rowindex, self.rowindex + self.m):
					self.map[(i, self.colindex)] = "*"

				self.rowindex += self.m
				self.m = 0
				self.sweep()

		elif (self.m == coldiff * rowdiff - 1):
			for i in range(self.rowindex, self.r):
				for j in range(self.colindex, self.c):
					if (i == (self.r - 1) and j == (self.c - 1)):
						self.map[(i, j)] = "c"
					else:
						self.map[(i, j)] = "*"

			self.m = 0

		elif (coldiff == 2 or rowdiff == 2):
			#print "either one is 2"
			# if (self.m % 2 == 1):
			# 	print "here bs"
			# 	self.impossible = True

			clear = coldiff * rowdiff - self.m
			if (clear >= 4 and clear % 2 == 0):
				bomblines = self.m / 2
				#print "here at 2, bomblines", bomblines
				if (rowdiff == 2):
					for i in range(self.rowindex, self.r):
						for j in range(self.colindex, self.colindex + bomblines):
							self.map[(i, j)] = "*"

					self.colindex += bomblines
					self.m = 0
					self.sweep()

				elif (coldiff == 2):
					for i in range(self.rowindex, self.rowindex + bomblines):
						for j in range(self.colindex, self.c):
							self.map[(i, j)] = "*"

					self.rowindex += bomblines
					self.m = 0
					self.sweep()
			
			else:
				self.impossible = True

		elif (self.m > coldiff * rowdiff - 4):
			#print "not possible cuz too many"
			self.impossible = True

		elif (coldiff >= rowdiff):
			if (self.m >= coldiff):
				if ((self.m % coldiff == 0 or self.m % rowdiff != 0) and (coldiff - self.m / coldiff) >= 2):
					self.fillrow(rowdiff, coldiff)
				else:
					self.fillcol(rowdiff, coldiff)

			elif (self.m >= rowdiff):
				self.fillcol(rowdiff, coldiff)

			else:
				if ((coldiff - self.m) >= 2):
					self.partialrow2(rowdiff, coldiff)
				elif ((rowdiff - self.m) >= 2):
					self.partialcol2(rowdiff, coldiff)
				elif ((coldiff - self.m) == 1):
					self.partialrow1(rowdiff, coldiff)
				elif ((rowdiff - self.m) == 1):
					self.partialcol1(rowdiff, coldiff)

		elif (coldiff < rowdiff):
			if (self.m >= rowdiff):
				if ((self.m % rowdiff == 0 or self.m % coldiff != 0) and (rowdiff - self.m / rowdiff) >= 2):
					self.fillcol(rowdiff, coldiff)
				else:
					self.fillrow(rowdiff, coldiff)

			elif (self.m >= coldiff):
				self.fillrow(rowdiff, coldiff)

			else:
				if ((rowdiff - self.m) >= 2):
					self.partialcol2(rowdiff, coldiff)
				elif ((coldiff - self.m) >= 2):
					self.partialrow2(rowdiff, coldiff)
				elif ((rowdiff - self.m) == 1):
					self.partialcol1(rowdiff, coldiff)
				elif ((coldiff - self.m) == 1):
					self.partialrow1(rowdiff, coldiff)				

	def fillcol(self, rowdiff, coldiff):
		bomblines = min(min(self.m / rowdiff, coldiff - 2), 1)
		for i in range(self.rowindex, self.r):
			for j in range(self.colindex, self.colindex + bomblines):
				self.map[(i, j)] = "*"

		self.colindex += bomblines
		self.m -= rowdiff * bomblines
		self.sweep()

	def fillrow(self, rowdiff, coldiff):
		bomblines = min(min(self.m / coldiff, rowdiff - 2), 1)
		for i in range(self.rowindex, self.rowindex + bomblines):
			for j in range(self.colindex, self.c):
				self.map[(i, j)] = "*"

		self.rowindex += bomblines
		self.m -= coldiff * bomblines
		self.sweep()

	def partialrow2(self, rowdiff, coldiff):
		for i in range(self.colindex, self.colindex + self.m):
			self.map[(self.rowindex, i)] = "*"
		for i in range(self.colindex + self.m, self.c):
			self.map[(self.rowindex, i)] = "."

		self.rowindex += 1
		self.m = 0
		self.sweep()

	def partialcol2(self, rowdiff, coldiff):
		for i in range(self.rowindex, self.rowindex + self.m):
			self.map[(i, self.colindex)] = "*"
		for i in range(self.rowindex + self.m, self.r):
			self.map[(i, self.colindex)] = "."

		self.colindex += 1
		self.m = 0
		self.sweep()

	def partialrow1(self, rowdiff, coldiff):
		for i in range(self.colindex, self.colindex + self.m - 1):
			self.map[(self.rowindex, i)] = "*"
		self.map[(self.rowindex, self.c - 1)] = "." 
		self.map[(self.rowindex, self.c - 2)] = "."

		self.rowindex += 1
		self.m = 1
		self.sweep()

	def partialcol1(self, rowdiff, coldiff):
		for i in range(self.rowindex, self.rowindex + self.m - 1):
			self.map[(i, self.colindex)] = "*"
		self.map[(self.r - 1, self.colindex)] = "."
		self.map[(self.r - 2, self.colindex)] = "."

		self.colindex += 1
		self.m = 1
		self.sweep()

#input = "C-small-attempt0.in"
input = "C-small-attempt1.in"
with open(input) as myfile:
	lines = myfile.read().splitlines();

count = int(lines[0])
#print count
#myfile = open('C-small-attempt0.out','w')
myfile = open('C-small-attempt1.out','w')
for index in range(count):
		rcm = lines[index + 1].split(" ")
		r = int(rcm[0])
		c = int(rcm[1])
		m = int(rcm[2])
		#print "case # ", index + 1

		ms = MineSweeper(c, r, 0, 0, m)
		ms.sweep()
		output = ms.get_output()

		myfile.write("Case #{}:\n".format(index + 1))
		myfile.write(output)
		

myfile.close()