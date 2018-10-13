import sys

if __name__=="__main__":
	f = open(sys.argv[1])
	cases = int(f.readline())
	for case in xrange(1, cases+1):
		pairs = []
		for i in xrange(int(f.readline())):
			x, y = map(int, f.readline().split())
			pairs.append((x, y))
		pairs.sort()
		crosses = 0
		for i, (x,y) in enumerate(pairs):
			k = i+1
			while k < len(pairs) and pairs[k][1] < y:
				crosses += 1
				k += 1
		print "Case #%d: %d" % (case, crosses)
