import sys

output = open('output.out', 'w')
File = open(sys.argv[1], 'r')

count = 0
readCount = 0

class Lawn():

	def __init__(self, dataList, count):
		self.x = int(dataList[0])
		self.y = int(dataList[1])
		self.count = count + 1
		self.data = []
		self.inputData()
		self.dataMap = {}

	def inputData(self):
		global File
		for i in range(self.x):
			line = map(int, File.readline().strip().split(" "))
			self.data.append(line)

	def getDataMap(self):
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				key = self.data[i][j]
				if self.data[i][j] in self.dataMap:
					self.dataMap[key].append([i, j])
				else:
					self.dataMap[key] = []
					self.dataMap[key].append([i, j])

	def rowValid(self, coord):
		x = coord[0]
		y = coord[1]
		for i in range(y):
			if self.data[x][i] > self.data[x][y]:
				return False
		for i in range(y, self.y):
			if self.data[x][i] > self.data[x][y]:
				return False
		return True

	def columnValid(self, coord):
		x = coord[0]
		y = coord[1]
		for i in range(x):
			if self.data[i][y] > self.data[x][y]:
				return False
		for i in range(x, self.x):
			if self.data[i][y] > self.data[x][y]:
				return False
		return True

	def trimEdge(self, coordList):
		centered = []
		edged = []
		for item in coordList:
			if item[0] > 0 and item[1] > 0 and item[0] < self.x - 1 and item[1] < self.y - 1:
				centered.append(item)
			# elif item[0] != self.x - 1 and item[1] != self.y - 1:
			# 	centered.append(item)
			else:
				edged.append(item)
		return [centered, edged]

	def trimColumn(self, coord, pair, list):
		x = coord[0]
		y = coord[1]
		# print [x, y] in list
		for i in range(x):
			# print i, y
			if [i, y] in pair:
				# print "in pair"
				pair.remove([i, y])
			if [i, y] in list:
				# print "in list"
				list.remove([i, y])
		for i in range(x, self.x):
			if [i, y] in pair:
				pair.remove([i, y])
			if [i, y] in list:
				list.remove([i, y])

	def trimRow(self, coord, pair, list):
		x = coord[0]
		y = coord[1]
		# print "target:", coord
		for i in range(y):
			# print x, i
			if [x, i] in pair:
				pair.remove([x, i])
			if [x, i] in list:
				list.remove([x, i])
		for i in range(y, self.y):
			# print x, i
			if [x, i] in pair:
				pair.remove([x, i])
			if [x, i] in list:
				list.remove([x, i])

	def isPossible(self, coordList):
		tmpList = list(coordList)
		pair = self.trimEdge(tmpList)
		while len(tmpList) > 0:
			while len(pair[0]) > 0:
				# print pair[0]
				target = pair[0][0]
				if not self.rowValid(target) and not self.columnValid(target):
					return False
				if self.rowValid(target):
					self.trimRow(target, pair[0], tmpList)
				if self.columnValid(target):
					self.trimColumn(target, pair[0], tmpList)
			while len(pair[1]) > 0:
				# print pair[1]
				target = pair[1][0]
				if not self.rowValid(target) and not self.columnValid(target):
					return False
				if self.rowValid(target):
					self.trimRow(target, pair[1], tmpList)
				if self.columnValid(target):
					# print "ss"
					self.trimColumn(target, pair[1], tmpList)
		return True

	def start(self):
		keyList = self.dataMap.keys()
		global output
		head = "Case #"+str(self.count)+": "
		for i in range(len(keyList) - 2, -1, -1):
			key = keyList[i]
			coordList = self.dataMap[key]
			if not self.isPossible(coordList):
				output.write(head + "NO" + "\n")
				print "NO"
				return
		output.write(head + "YES" + "\n")
		print "YES"


	def run(self):
		self.getDataMap()
		self.start()

case = int(File.readline().strip())
for i in range(case):
	data = File.readline().strip().split(" ")
	lawn = Lawn(data, i)
	lawn.run()
		
File.close()
output.close()