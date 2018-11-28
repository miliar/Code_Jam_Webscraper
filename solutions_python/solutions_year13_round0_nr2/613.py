class Board:
	def __init__(self):
		self.rows = []
		self.hasemptyfield = False

	def addRow(self, line):
		self.rows.append([int(n) for n in line.strip().split()])

	def getRow(self, index):
		return self.rows[index]

	def getRowMax(self, index):
		row = self.rows[index]
		return max(row)

	def getColMax(self, index):
		column = []
		rows = len(self.rows)
		for i in range(0, rows):
			column.append(self.rows[i][index])
		return max(column)

	def solve(self):
		N = len(self.rows)
		M = len(self.rows[0])
		
		for i in range(0, N):
			rowmax = self.getRowMax(i)
			for j in range(0, M):
				colmax = self.getColMax(j)
				data = self.rows[i][j]
				if (data >= rowmax or data >= colmax) == False:
					return False
		
		return True

	def clear(self):
		self.rows = []
		self.hasemptyfield = False
	
	def getLength(self):
		return len(self.rows)
	
f = open('B-large.in')
output = open('B_large_output.txt', 'w')

def echo(line):
	print line
	output.write(line + '\n')

n = 0
k = 0
board = Board()
cases = int(f.readline())

N = 0
M = 0

for line in f:
	fields = line.strip().split(' ')
	if N == 0 or N == n - 1:
		N = int(fields[0])
		M = int(fields[1])
		n = 0
		k += 1

	if (N == 0 or n - 1 < N) and n > 0:
		board.addRow(line)

	if n > 0 and board.getLength() == N:
		result = board.solve()
		board.clear()
		answer = 'YES'
		if result == False:
			answer = 'NO'
		echo('Case #' + str(k) + ': ' + answer)

	n += 1

f.close()
output.close()
