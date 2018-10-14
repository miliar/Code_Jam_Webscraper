#code Challenge
from numpy import *

class Prob1():
	
	def __init__(self):
		self.numTests = 0
		self.matrix = zeros( (4,4) )
		self.goal = [0,0,0,0]
		self.curTest = 0
		self.sel_row = 0

	def findNum(self):
		temp = 0
		key = 0
		result = 9
		for i in xrange(4):
			for j in xrange(4):
				key = int(self.goal[i])
				search = int(self.matrix[self.sel_row][j])
				if key == search:
					temp += 1
					result = key
		if temp == 1:
			s = "Case #" + str(self.curTest) + ": " + str(result)
			print s
		if temp > 1:
			s = "Case #" + str(self.curTest) + ": Bad magician!" 
			print s
		if temp == 0:
			s = "Case #" + str(self.curTest) + ": Volunteer cheated!"
			print s

	def readFile(self):
		filename = 'prob1.txt'
		f = open(filename, 'r')
		self.numTest = int(f.readline())
		for i in xrange(self.numTest):
			self.curTest += 1
			self.sel_row = int(f.readline()) - 1 
			#build the matrix
			for j in xrange(4):
				k = 0
				for s in f.readline().split(" "):
					self.matrix[j][k] = int(s)
					k += 1
			#print self.matrix
			#get the user input

			for j in xrange(4):
				temp = self.matrix[self.sel_row][j]
				self.goal[j] = temp
			
			#read in second number
			self.sel_row = int(f.readline()) - 1
			#read in the matrix again
			#build the matrix
			for j in xrange(4):
				k = 0
				for s in f.readline().split(" "):
					self.matrix[j][k] = int(s)
					k += 1
			#print self.matrix
			#now find out the number if we can.
			self.findNum()

hello = Prob1()
hello.readFile()