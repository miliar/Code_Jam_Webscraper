class comparator:
	Xcount = 0
	Ocount = 0
	emptyspace = 0
	result = ''
	def compare(self,next): 
		if next == 'X':
			self.Xcount += 1
			self.Ocount = 0
			if self.Xcount >= 4:
				self.result = "X won"
				return 1
		elif next == 'O':
			self.Xcount = 0
			self.Ocount += 1
			if self.Ocount >= 4:
				self.result = "O won"
				return 1
		elif next == '.':
			self.Xcount = 0
			self.Ocount = 0
			self.emptyspace = 1
		elif next == 'T':
			self.Xcount += 1
			self.Ocount += 1
			if self.Xcount >=4:
				self.result = "X won"
				return 1
			if self.Ocount >=4:
				self.result = "O won"
				return 1
		return 0
	def reset(self):
		self.Xcount = 0
		self.Ocount = 0

def tictac(grid):
	# check for vertical/horizontal win
	vertical = comparator()
	horizontal = comparator()
	for i in range(4):
		for j in range(4):
			if vertical.compare(grid[i][j]) == 1:
				#print "{} {}".format(vertical.Xcount, vertical.Ocount)
				return vertical.result
			if horizontal.compare(grid[j][i]) == 1:
				return horizontal.result
		vertical.reset()
		horizontal.reset()
		
	# only two diagonal wins possible
	diag1 = comparator()
	diag2 = comparator()
	for i in range(4):
		if diag1.compare(grid[i][i]) == 1:
			return diag1.result
		if diag2.compare(grid[i][4-i-1]) == 1:
			return diag2.result
	
	#no wins found
	if vertical.emptyspace == 1:
		return "Game has not completed"
	else:
		return "Draw"
	
f = open('A-large.in', 'r')
T = int(f.readline())
for i in range(T):
	grid = [[] for j in range(4)]
	for k in range(4):
		grid[k] = list(f.readline())
	f.readline()
	print "Case #{}: {}".format(i+1, tictac(grid))