import sys
import math

def run(N,K,xs):
	xs.sort()

	def area(r):
		return math.pi * r * r

	def sides(r,h):
		return 2 * math.pi * r * h

	def sub(i):
		ret  = area(xs[i][0]) + sides(xs[i][0], xs[i][1])
		ys   = list(reversed(sorted([sides(x[0],x[1]) for x in xs[:i]])))
		ret += sum(ys[:(K-1)])

		return ret

	return max(sub(i) for i in xrange(K-1,N))

if __name__ == '__main__':
	T = int(raw_input())
	for t in xrange(T):
		(N,K) = map(int, raw_input().split())
		xs = []
		for i in xrange(N):
			(r,k) = map(float, raw_input().split())
			xs.append((r,k))

		print "Case #%d: %.9f" % (t+1, run(N,K,xs))
