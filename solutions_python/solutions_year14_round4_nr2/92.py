#!/usr/bin/env python

#FILE_NAME_BASE = 'B-example'
#FILE_NAME_BASE = 'B-small-attempt1'
FILE_NAME_BASE = 'B-large'
NUM_PROCESSES = 4
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

def parse(inp):
	n, = (int(x) for x in inp.readline().split())
	numbers = tuple(int(x) for x in inp.readline().split())
	assert len(numbers) == n
	return numbers,

def solve(a):
	a = list(a)
	fwd = sorted(enumerate(a), key = lambda p: p[1])
	ns = [
		sum(a[j] < v for j in xrange(i))
		for i, v in enumerate(a)
		]

	swaps = 0
	l = 0
	r = len(a)
	for f, (i, _) in enumerate(fwd):
		ri = i - ns[i]
		sl = ri
		sr = r - l - ri - 1
		if sl < sr:
			swaps += sl
			l += 1
		else:
			swaps += sr
			r -= 1

	assert l == r
	return swaps

def main():
	import sys
	sys.setrecursionlimit(RECURSION_LIMIT)

	import resource
	soft, hard = resource.getrlimit(resource.RLIMIT_AS)
	resource.setrlimit(resource.RLIMIT_AS, (MEM_LIMIT_GB * 1024 ** 3, hard))

	inp = open(FILE_NAME_BASE + '.in', 'r')
	numCases = int(inp.readline())
	if NUM_PROCESSES == 0:
		results = [
			solve(*parse(inp))
			for _ in range(numCases)
			]
	else:
		from multiprocessing import Pool
		pool = Pool(NUM_PROCESSES)
		results = [
			pool.apply_async(solve, parse(inp))
			for _ in range(numCases)
			]
	inp.close()
	out = open(FILE_NAME_BASE + '.out', 'w')
	for case, result in enumerate(results):
		value = result if NUM_PROCESSES == 0 else result.get()
		out.write('Case #%d: %s\n' % (case + 1, value))
		out.flush()
	out.close()

if __name__ == '__main__':
	main()
