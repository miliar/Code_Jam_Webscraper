#!/usr/bin/env python

from collections import defaultdict

FILE_NAME_BASE = 'A-large'
NUM_PROCESSES = 4
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

def parse(inp):
	nstops, npairs = (int(x) for x in inp.readline().split())
	travel = []
	for _ in xrange(npairs):
		origin, end, passengers = (int(x) for x in inp.readline().split())
		travel.append((origin - 1, end - 1, passengers))
	return nstops, travel

def solve(nstops, travel):
	mod = 1000002013

	enterDict = defaultdict(int)
	for o, e, p in travel:
		enterDict[o] += p
	enter = sorted(enterDict.iteritems())

	leaveDict = defaultdict(int)
	for o, e, p in travel:
		leaveDict[e] += p
	leave = sorted(leaveDict.iteritems())

	#print enter, leave

	el = len(enter)
	ei = 0
	ontrain = []
	paid = 0
	for stop, pl in leave:
		while ei < el and enter[ei][0] <= stop:
			ontrain.append(enter[ei])
			ei += 1

		while pl > 0:
			o, p = ontrain.pop()
			if p > pl:
				left = pl
				ontrain.append((o, p - left))
			else:
				left = p
			pl -= left
			n = stop - o
			price = n * nstops - (n * (n - 1)) / 2
			paid = (paid + price * left) % mod

	expected = 0
	for o, e, p in travel:
		n = e - o
		price = n * nstops - (n * (n - 1)) / 2
		expected = (expected + price * p) % mod

	return (expected - paid) % mod

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
