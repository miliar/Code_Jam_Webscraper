import sys

def get_cycle_lengths(p):
	cycle_lengths = []
	marked = [False for x in p]
	length = 0
	for i in xrange(len(p)):
		if not marked[i]:
			j = i
			while True:
				if marked[j]:
					cycle_lengths.append(length)
					length = 0
					break
				else:
					length += 1
				marked[j] = True
				j = p[j] - 1
	return cycle_lengths


with open(sys.argv[1]) as f:
	T = int(f.readline())
	for testcase in xrange(T):
		N = int(f.readline())
		p = [int(x) for x in f.readline().split()]
		
		answer = 0
		for l in get_cycle_lengths(p):
			if l > 1:
				answer += l
		
		print 'Case #%d:' % (testcase + 1), answer
