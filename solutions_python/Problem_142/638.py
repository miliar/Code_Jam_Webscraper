import lib
import numpy as np
from sets import Set
import itertools

@lib.wrapper
def solution(input, output):
	T = input.int()
	for case in xrange(1,T+1):
		N = input.int()
		strings = [input.str() for _ in range(N)]
		
		unique_versions = [
			[k for k,g in itertools.groupby(string)]
			for string in strings]
		if all(x==unique_versions[0] for x in unique_versions):
			counts = np.array([
				[len(list(g)) for k,g in itertools.groupby(string)]
				for string in strings])
			average_count = np.average(counts, axis=0)
			changes = int(np.sum(np.abs(counts-np.round(average_count))))
			output.result(case, changes)
		else:
			output.result(case, "Fegla Won")

if __name__ == '__main__':
	solution("A-small-attempt0.in", "A-small-attempt0.out")
