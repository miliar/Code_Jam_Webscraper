from multiprocessing import Pool
import sys
from itertools import chain, combinations

class CodeJamAlgo:
	def __init__(self, i, o, algo, option_count, process_count, line_preprocessor=None):
		self.i = i
		self.o = o
		self.pool = Pool(process_count)
		self.algo = algo

		self.options = [self.i.readline() for i in range(option_count)]

		if line_preprocessor != None:
			self.i = line_preprocessor(self.i)

	def run(self):
		results = []
		for i in self.i:
			results.append(self.pool.apply_async(self.algo, (self.options, i)))

		for i in range(len(results)):
			self.o.write('Case #'+str(i+1) + ': ' +str(results[i].get()) + '\n')

def algoTest(options, args):
	return int(args) + 10

def algoTest2(options, args):
	return int(args[0]) + int(args[1])

def groupLines(i, count):
	lines = i.readlines()
	for j in range(len(lines)/count):
		yield lines[j*count:(j+1)*count]

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def badsum(cset):
	xor_lot = 0
	for i in cset:
		xor_lot = xor_lot^i
	return xor_lot

def algo_badcount(options, args):
	candyjar = [ int(x) for x in set(args[1].split(' '))]
	indices = set(range(len(candyjar)))

	found = False
	best = 0

	for first in powerset(indices):

		if len(first) == 0 or len(first) == len(candyjar):
			continue

		second = [candyjar[i] for i in indices.difference(first)]
		ffirst = [candyjar[i] for i in first]
		sum_first = sum(ffirst)
		
		if badsum(second) == sum_first:
			found = True
			if sum_first > best:
				best = sum_first
			if sum(second) > best:
				best = sum(second)

	if found:
		return best
	else:
		return 'NO'

if __name__ == '__main__':
	#CodeJamAlgo(sys.stdin, sys.stdout, algoTest, 0, 8).run()
	#CodeJamAlgo(sys.stdin, sys.stdout, algoTest2, 0, 8, lambda x : groupLines(x, 2)).run()
	#CodeJamAlgo(sys.stdin, sys.stdout, algo_store_credit, 1, 8, lambda x : groupLines(x, 3)).run()
	#CodeJamAlgo(sys.stdin, sys.stdout, algo_reverse_words, 1, 8).run()
	#CodeJamAlgo(sys.stdin, sys.stdout, algo_t9, 1, 8).run()
	#CodeJamAlgo(sys.stdin, sys.stdout, algo_msp, 1, 8, lambda x : groupLines(x, 3)).run()
	CodeJamAlgo(sys.stdin, sys.stdout, algo_badcount, 1, 8, lambda x : groupLines(x, 2)).run()
