class Stall:
	def __init__(self, occupied):
		self.occupied = occupied
		self.max = 0
		self.min = 0

	def SetPosition(self, position):
		self.position = position

	def SetOccupied(self, status):
		self.occupied = status

	def SetMinMax(self, leftO, rightO):
		if(not self.occupied):
			leftD = self.position - leftO - 1
			rightD = rightO - self.position - 1

			if(leftD > rightD):
				self.max = leftD
				self.min = rightD
			else:
				self.max = rightD
				self.min = leftD

class StallRow:
	def __init__(self, dimension):
		self.row = [Stall(True)]

		for i in range(dimension):
			self.row.append(Stall(False))
		
		self.row.append(Stall(True))

		self.occuppies = [0, len(self.row)-1]

		self.SetPosition()
		self.UpdateStall(0)

	def SetPosition(self):
		for i in range(len(self.row)):
			self.row[i].SetPosition(i)

	def UpdateStall(self, position):
		mo = position
		for i in range(self.occuppies[mo], len(self.row)):
			if(mo + 1 < len(self.occuppies)-1 and self.occuppies[mo + 1] <= i):
				mo += 1

			self.row[i].SetMinMax(self.occuppies[mo], self.occuppies[mo + 1])

	def SetOccupied(self, position):
		self.row[position].SetOccupied(True)
		prev = 0
		
		for i in range(1, len(self.occuppies)):
			if(self.occuppies[i-1] < self.row[position].position and self.occuppies[i] > self.row[position].position):
				prev = i-1
				self.occuppies.insert(i, position)
		self.UpdateStall(prev)

t = int(input())
n = []
s = []

for i in range(t):
	blah = input()
	n.append(blah.split(" "))
	n[i][0] = int(n[i][0])
	n[i][1] = int(n[i][1])
	s.append(StallRow(n[i][0]))

for i in range(len(s)):
	last_position = -1
	for o in range(n[i][1]):
		position = -1
		for e in range(len(s[i].row)):
			if(not s[i].row[e].occupied):
				if(position == -1 or s[i].row[e].min > s[i].row[position].min):
					position = e
				elif(s[i].row[e].min == s[i].row[position].min and s[i].row[e].max > s[i].row[position].max):
					position = e
		s[i].SetOccupied(position)
		last_position = position
	print("Case #%d: %d %d" % (i+1, s[i].row[position].max, s[i].row[position].min))