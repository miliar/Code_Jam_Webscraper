from itertools import combinations
import os

class ProblemA(object):

	def __init__(self, file='test.in'):
		self.next = open(file).next

	def solve(self):
		n = int(self.next())
		wires = [ map(int, self.next().split())  for x in range(n)]

		count = 0
		for a,b in combinations(wires, 2):
			if a[0] > b[0] and a[1] < b[1]: count += 1
			if a[0] < b[0] and a[1] > b[1]: count += 1

		return count

	def run(self):
		n = int(self.next())

		with open('result.txt', 'w') as f:
			for i in range(n):
				result = 'Case #%d: %s'%(i+1, self.solve())
				print result
				f.write(result + '\n')

if __name__ == '__main__':
	ProblemA('A-large.in').run()
