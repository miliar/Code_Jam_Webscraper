import os

class ProblemA(object):

	def __init__(self, file='test.in'):
		self.next = open(file).next

	def solve(self):
		N, M = map(int, self.next().split())

		exist = [ self.next().strip() for x in range(N) ]
		make  = [ self.next().strip() for x in range(M) ]

		leaf_list = []

		count = 0

		for _dir in make:
			while _dir != '/':
				if _dir in exist:
					exist.extend(leaf_list)
					exist = list(set(exist))
					break
				odir = _dir
				_dir, leaf  = os.path.split(_dir)
				if odir not in leaf_list:
					leaf_list.append(odir)

		return len(leaf_list)

	def run(self):
		n = int(self.next())

		with open('result.txt', 'w') as f:
			for i in range(n):
				result = 'Case #%d: %s'%(i+1, self.solve())
				print result
				f.write(result + '\n')

if __name__ == '__main__':
	ProblemA('A-large.in').run()
