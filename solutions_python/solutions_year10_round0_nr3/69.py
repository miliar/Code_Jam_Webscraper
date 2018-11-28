import sys
import psyco
psyco.full()
def dbg(a): sys.stderr.write(str(a))
def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(foo): return [foo(x) for x in raw_input().split()]

def run_test(test):
	dbg("Test %d\n" % (test + 1))
	(R, k, N) = readarray(int)
	a = readarray(int)
	skip = []
	cost = []
	for i in xrange(N):
		s = 0
		c = 0
		for j in xrange(N + 1):
			next = (i + j) % N
			s += a[next]
			if j == N or s > k:
				skip.append(j)
				cost.append(s - a[next])
				break
	res = 0
	pos = 0
	for i in xrange(R):
		res += cost[pos]
		pos = (pos + skip[pos]) % N
	
	print "Case #%d: %d" % (test + 1, res)

for test in range(readint()):
	run_test(test)

