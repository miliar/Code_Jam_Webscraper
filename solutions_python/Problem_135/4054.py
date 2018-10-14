import sys, os

class Problem:
	def __init__(self, case_number):
		self.grid1 = []
		self.grid2 = []
		self.row1 = 0
		self.row2 = 0
		self.case_number = case_number

	def is_complete(self):
		if not self.row1 or not self.row2:
			return False
		if len(self.grid1) != 4 or len(self.grid2) != 4:
			return False
		for i in range(0, 4):
			if len(self.grid1[i]) != 4 or len(self.grid2[i]) != 4:
				return False
		return True

	def read(self, fd):
		line = fd.readline().strip('\n')
		self.row1 = int(line)
		for _ in range(0, 4):
			line = fd.readline().strip('\n')
			row = map((lambda i : int(i)), line.split())
			self.grid1.append(row)
		line = fd.readline().strip('\n')
		self.row2 = int(line)
		for _ in range(0, 4):
			line = fd.readline().strip('\n')
			row = map((lambda i : int(i)), line.split())
			self.grid2.append(row)

	def solve(self):
		if not self.is_complete():
			return "Problem incomplete."
		row1 = self.grid1[self.row1-1]
		row2 = self.grid2[self.row2-1]
		common_cards = [card for card in row1 if card in row2]
		prefix = "Case #" + str(self.case_number) + ': '
		if not common_cards:
			return prefix + 'Volunteer cheated!'
		if len(common_cards) > 1:
			return prefix + 'Bad magician!'
		return prefix + str(common_cards[0])

	def __str__(self):
		if not self.is_complete():
			return "Problem incomplete."
		s = ''
		for r, g in [(self.row1, self.grid1), (self.row2, self.grid2)]:
			s += str(r) + '\n'
			for row in g:
				for val in row:
					s += str(val) + ' '
				s += '\n'
		s += '\n'
		return s 

def parse_input(path):
	problems = []
	with open(path, 'r') as f:
		line = f.readline().strip('\n')
		problem_number = int(line)
		for case_number in range(0, problem_number):
			problem = Problem(case_number+1)
			problem.read(f)
			problems.append(problem)
	return problems

# get input path
path = sys.argv[1] if len(sys.argv) > 1 else 'A-small-attempt0.in'
problems = parse_input(path)
with open('output.txt', 'w') as f:
	for problem in problems:
		f.write(problem.solve())
		f.write('\n')