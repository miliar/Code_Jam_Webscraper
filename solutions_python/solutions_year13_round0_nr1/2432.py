import sys

class input(object):
	def __init__(self):
		self.boards = []
		lines = sys.stdin.readlines()
		num = int(lines[0].strip())
		for c in range(1, num + 1):
			i = (c-1)*5
			l1 = lines[i+1].strip()
			l2 = lines[i+2].strip()
			l3 = lines[i+3].strip()
			l4 = lines[i+4].strip()
			b = board(l1, l2, l3, l4)
			r = b.test()
			print('Case #%d: %s' % (c, r))
			

class board(object):
	def __init__(self, l1, l2, l3, l4):
		self.data = [['','','',''], ['','','',''],['','','',''],['','','','']]
		for i in range(0, 4):
			self.data[0][i]=l1[i]
			self.data[1][i]=l2[i]
			self.data[2][i]=l3[i]
			self.data[3][i]=l4[i]

	def test(self):
		r = self.testMainDiag()
		if r == 'X':
			return 'X won'
		if r == 'O':
			return 'O won'
		r = self.testSecondDiag()
		if r == 'X':
			return 'X won'
		if r == 'O':
			return 'O won'
		fulls = 0
		for r in range(4):
			r = self.testRow(r)
			if r == 'X':
				return 'X won'
			if r == 'O':
				return 'O won'
			if r == 'F':
				fulls = fulls + 1
		for r in range(4):
			r = self.testColumn(r)
			if r == 'X':
				return 'X won'
			if r == 'O':
				return 'O won'
		if fulls == 4:
			return 'Draw'
		return 'Game has not completed'

	def testMainDiag(self):
		c1 = self.data[0][0]
		c2 = self.data[1][1]
		c3 = self.data[2][2]
		c4 = self.data[3][3]
		return self.testPos(c1, c2, c3, c4)

	def testSecondDiag(self):
		c1 = self.data[3][0]
		c2 = self.data[2][1]
		c3 = self.data[1][2]
		c4 = self.data[0][3]
		return self.testPos(c1, c2, c3, c4)

	def testRow(self, r):
		c1 = self.data[r][0]
		c2 = self.data[r][1]
		c3 = self.data[r][2]
		c4 = self.data[r][3]
		r = self.testPos(c1, c2, c3, c4)
		return r

	def testColumn(self, c):
		c1 = self.data[0][c]
		c2 = self.data[1][c]
		c3 = self.data[2][c]
		c4 = self.data[3][c]
		r = self.testPos(c1, c2, c3, c4)
		return r

	def testPos(self, c1, c2, c3, c4):
		if c1 in ('T', 'X') and c2 in ('T','X') and c3 in ('T','X') and c4 in ('T','X'):
			return 'X'
		if c1 in ('T', 'O') and c2 in ('T','O') and c3 in ('T','O') and c4 in ('T','O'):
			return 'O'
		if c1 in ('T', 'O','X') and c2 in ('T','O','X') and c3 in ('T','O','X') and c4 in ('T','O','X'):
			return 'F'
		return None
				
i = input()

