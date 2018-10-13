class ThemePark(object):
	
	def __init__(self, file='test.in'):
		self.next = open(file).next

	def solve(self):
		"""
		coast per ride : 1 Euros
		k : max passengers per ride
		R : rides per a day
		"""
		R, k, N = map(int, self.next().split())
		groups  = map(int, self.next().split())

		assert len(groups) == N

		profit = 0
		ride = []
		for i in range(R):
			while True:
				if not groups or sum(ride) + groups[0] > k:
					groups.extend(ride)
					ride = []
					break
				n = groups.pop(0)
				ride.append(n)
				profit += n	
		return profit	
	
	def run(self):
		n = int(self.next())

		with open('result.txt', 'w') as f:
			for i in range(n):
				result = self.solve()
				result_s = 'Case #%d: %s'%(i+1, result)
				print result_s
				f.write(result_s + '\n')

if __name__ == '__main__':
	ThemePark(file='C-small-attempt0.in').run()
