import sys
import heapq
import collections

def run(N,K):
	counts = collections.defaultdict(lambda: 0)
	queue  = [-N]

	counts[N] = 1

	def split_seg(sz):
		if sz % 2 == 0:
			return (sz/2-1, sz/2)
		else:
			return (sz/2, sz/2)

	while K > 0:
		sz = -heapq.heappop(queue)
		if sz not in counts:
			continue

		cn = counts[sz]
		del counts[sz]

		assert cn > 0

		(a,b) = split_seg(sz)
		if cn < K:
			K -= cn
			counts[a] += cn
			counts[b] += cn
			heapq.heappush(queue, -a)
			heapq.heappush(queue, -b)
		else:
			return (max(a,b),min(a,b))

	assert False

def smoke():
	import random

	for k in xrange(1000):
		n = random.randint(100000,999999)
		a = brute(n)
		b = run(n)
		print "%d: %d <-> %d" % (n,a,b)
		assert a == b

if __name__ == '__main__':
	#smoke()
	#sys.exit(0)

	T = int(raw_input())
	for t in xrange(T):
		(N,K) = map(int, raw_input().split())
		(a,b) = run(N,K)
		print "Case #%d: %d %d" % (t+1,a,b)
