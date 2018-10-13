class SnapperChain(object):
	
	def __init__(self, file='A-small-attempt1.in'):
		self.next = open(file).next

	def solve(self):
		"""
			K : 10   N: 10
			
			K = 1 : 0000000001
			K = 2 : 0000000010
			K = 3 : 0000000011
			K = 4 : 0000000100
		"""
		N, K  = map(int, self.next().split())
		return {False:'OFF', True:'ON'}['1'*N == (bin(K)[2:])[-N:]]

	def run(self):
		n = int(self.next())

		with open('result.txt', 'w') as f:
			for i in range(n):
				result = self.solve()
				result_s = 'Case #%d: %s'%(i+1, result)
				f.write(result_s + '\n')

if __name__ == '__main__':
	SnapperChain(file='A-large.in').run()
