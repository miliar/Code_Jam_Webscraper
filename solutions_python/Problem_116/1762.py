import sys

output = open('output.out', 'w')
File = open(sys.argv[1], 'r')
count = 0
case = 0
data = []

class Game():

	def __init__(self, data, case):
		self.data = data
		self.case = case + 1
		self.xWind = False
		self.oWind = False
				
	def probeRow(self, i, j, symbol):
		if symbol == '.':
			return False
		tmp = True
		for index in range(j, len(self.data[i])):
			# print self.data[i][index]
			tmp = tmp & (self.data[i][index] == symbol or self.data[i][index] == 'T')
		if tmp:
			if symbol == 'X':
				self.xWind = True
			elif symbol == 'O':
				self.oWind = True
		# print tmp
		return tmp
	
	def probeColumn(self, i, j, symbol):
		if symbol == '.':
			return False
		tmp = True
		for index in range(i, len(self.data)):
			tmp = tmp & (self.data[index][j] == symbol or self.data[index][j] == 'T')
		if tmp:
			if symbol == 'X':
				self.xWind = True
			elif symbol == 'O':
				self.oWind = True
		return tmp

	def probeDown(self, i, j, symbol):
		if symbol == '.':
			return False
		tmp = True
		for index in range(i, len(self.data)):
			tmp = tmp & (self.data[index][index] == symbol or self.data[index][index] == 'T')
		if tmp:
			if symbol == 'X':
				self.xWind = True
			elif symbol == 'O':
				self.oWind = True
		return tmp

	def probeUp(self, i, j, symbol):
		if symbol == '.':
			return False
		# print i, j, symbol
		tmp = True
		for index in range(j, len(self.data)):
			tmp = tmp & (self.data[3-index][index] == symbol or self.data[3-index][index] == 'T')
		if tmp:
			if symbol == 'X':
				self.xWind = True
			elif symbol == 'O':
				self.oWind = True
		return tmp
		
	def probe(self, i, j):
		symbol = data[i][j]
		# print symbol
		if symbol != 'T':
			if i == 0 and j == 0:
				if self.probeRow(i, j, symbol):
					return
				if self.probeColumn(i, j, symbol):
					return
				if self.probeDown(i, j, symbol):
					return
			elif i == 3:
				if self.probeRow(i, j, symbol):
					return
				if self.probeUp(i, j, symbol):
					return
			else:
				if self.probeRow(i, j, symbol):
					return
		else:
			if i == 0 and j == 0:
				if self.probeRow(0, 1, self.data[0][1]):
					return
				if self.probeColumn(1, 0, self.data[1][0]):
					return
				if self.probeDown(1, 1, self.data[1][1]):
					return
			elif i == 3:
				if self.probeRow(3, 1, self.data[3][1]):
					return
				if self.probeUp(2, 1, self.data[2][1]):
					return
			else:
				if self.probeRow(i, j + 1, self.data[i][j + 1]):
					return

	def secondProbe(self, i, j):
		symbol = data[i][j]
		if symbol != 'T':
			if self.probeColumn(i, j, symbol):
				return
		else:
			if self.probeColumn(i + 1, j, self.data[i + 1][j]):
				return

	def judge(self):
		for i in range(len(self.data)):
			if self.data[i][0] != '.':
				# print "data:", self.data[i][0]
				self.probe(i, 0)

		for i in range(1,len(self.data[0])):
			self.secondProbe(0, i)

	def isComplete(self):
		for row in self.data:
			if '.' in row:
				return False
		return True

	def run(self):
		result = ""
		self.judge()
		head = "Case #"+str(self.case)+": "
		if not self.xWind and not self.oWind:
			if self.isComplete():
				result = head + "Draw"
			else:
				result = head + "Game has not completed"
		elif self.xWind:
			result = head + "X won"
		else:
			result = head + "O won"

		global output	
		output.write(result + "\n")
			

for line in File:
	if case < 1000:
		if count != 0:
			datalist = list(line.strip())
			data.append(datalist)
		count = count + 1
		if count == 5:
			# global case
			game = Game(data, case)
			count = 0
			case = case + 1
			game.run()
			data = []

		
File.close()
output.close()