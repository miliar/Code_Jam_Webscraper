import heapq
class Part(object):
	def __cmp__(self, other):
		if (self.r - self.l) > (other.r - other.l):
			return -1
		if (self.r - self.l) < (other.r - other.l):
			return 1
		if (self.r - self.l) == (other.r - other.l):
			if self.l < other.l:
				return -1
			else:
				return 1
	def size(self):
		return self.r - self.l

	def __init__(self, l, r):
		self.l = l
		self.r = r

	def __str__(self):
		return "{}-{}".format(self.l, self.r)

def solve(N, K):

	queue = [Part(0, N)]
	heapq.heapify(queue)
	while(K>1):
		gr = heapq.heappop(queue)
		size = gr.size()
		fstart = gr.l
		fend = fstart + (size/2) -1 if (size % 2 == 0) else fstart + (size/2)
		sstart = fend+1
		send = gr.r
		heapq.heappush(queue, Part(fstart, fend))
		heapq.heappush(queue, Part(sstart, send))

		K -= 1

	last = heapq.heappop(queue)

	t_min = last.size()/2-1 if (last.size() % 2 == 0) else (last.size()/2)
	return last.size() / 2, t_min,

TT = int(raw_input())

for T in xrange(1, TT+1):
	N, K = map(int, raw_input().split(' '))
	t_max, t_min = solve(N, K)
	print "Case #{}: {} {}".format(T, t_max, t_min)