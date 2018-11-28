import sys
class ListMax:
	def __init__(self, l):
		#print 'init', l
		self.l = l
		self.cache = {}
		self.fcache = {}

	def till(self, i):
		assert i >= 0 and i < len(self.l), 'index out of range'
		if i == 0:
			return self.l[i]
		elif i in self.cache:
			return self.cache[i]
		else:
			r = max(self.till(i - 1), self.l[i])
			self.cache[i] = r
			return r

	def from_(self, i):
		assert i >= 0 and i < len(self.l), 'index out of range'
		if i == len(self.l) - 1:
			return self.l[i]
		elif i in self.fcache:
			return self.fcache[i]
		else:
			r = max(self.l[i], self.from_(i + 1))
			self.fcache[i] = r
			return r

class Finish: pass
p = sys.stdout.write

def test1():
	m = ListMax([2, 1, 4, 1, 3])
	#import pdb
	#pdb.set_trace()
	assert m.till(1) == 2, 'fail'
	assert m.from_(1) == 4, 'fail'
	assert m.till(2) == 4, 'fail'
	assert m.from_(2) == 4, 'fail'

if __name__ == '__main__':
	#test1()
	#sys.exit(0)
	T = int(raw_input())
	for c in xrange(T):
		p('Case #%d: ' % (c + 1))
		N, M = map(int, raw_input().split())

		mx = []
		for i in xrange(N):
			mx.append(map(int, raw_input().split()))

		try:
			id = {}
			jd = {}

			for i in xrange(N):
				id[i] = ListMax(mx[i])
			
			for j in xrange(M):
				jd[j] = ListMax(map(lambda x: x[j], mx))

			for i in xrange(N - 1):
				for j in xrange(M - 1):
					if mx[i][ j] < id[i].from_(j + 1) and mx[i][ j] < jd[j].from_(i + 1):
						p('NO')
						raise Finish
			for i in xrange(1, N):
				for j in xrange(1, M):
					if mx[i][j] < id[i].till(j - 1) and mx[i][ j] < jd[j].till(i - 1):
						p('NO')
						raise Finish
			for i in xrange(N - 1):
				for j in xrange(1, M):
					if mx[i][j] < id[i].till(j - 1) and mx[i][ j] < jd[j].from_(i + 1):
						p('NO')
						raise Finish
			for i in xrange(1, N):
				for j in xrange(M - 1):
					if mx[i][j] < id[i].from_(j + 1) and mx[i][ j] < jd[j].till(i - 1):
						p('NO')
						raise Finish


			'''
				for i in xrange(1, N - 1):
					for j in xrange(1, M - 1):
						if mx[i][ j] < rd[i].till(j - 1) \
							and mx[i][ j] < rd[i].from_(j + 1) \
							and mx[i][ j] < cd[j].till(i - 1)  \
							and mx[i][ j] < cd[j].from_(i + 1):
							p('NO')
							raise Finish
			'''

			p('YES')
		except Finish:
			pass
		p('\n')
