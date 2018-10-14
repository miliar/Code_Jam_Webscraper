from heapq import *
import copy
from math import log

LOG2 = log(2)

class PancakeState:
	def __init__(self, elapsed, pancakes):
		'''pancakes is a heap of the negative of the number of pancakes on each plate'''
		self.elapsed = elapsed
		self.pancakes = pancakes

	def get_next(self):
		elapsed = self.elapsed + 1
		next_states = [PancakeState(elapsed, [p+1 for p in self.pancakes])]
		maxpi = -heappop(self.pancakes)
		for i in range(1, maxpi/2+1):
			pancakes = copy.copy(self.pancakes)
			heappush(pancakes, -i)
			heappush(pancakes, i-maxpi)
			next_states.append(PancakeState(elapsed, pancakes))
		return next_states

	def is_goal(self):
		return -self.pancakes[0] <= 3

	def get_estimate(self):
		if self.is_goal():
			return self.elapsed - self.pancakes[0]
		else:
			return self.elapsed + log(-self.pancakes[0])/LOG2

def count_minutes(original_pancakes):
	pancakes = [-p for p in original_pancakes]
	heapify(pancakes)
	start_state = PancakeState(0, pancakes)
	frontier = [(start_state.get_estimate(), start_state)]

	while True:
		(est, state) = heappop(frontier)
		if state.is_goal():
			return state.get_estimate()
		else:
			next_states = state.get_next()
			for s in next_states:
				heappush(frontier, (s.get_estimate(), s))

def solve(testid):
	f = open(testid + '.in')
	g = open(testid + '.out', 'w')

	T = int(f.readline())

	for i in range(1,T+1):
		print i
		D = int(f.readline())
		original_pancakes = [int(u) for u in f.readline().split()]
		minutes = count_minutes(original_pancakes)

		g.write('Case #{}: {}\n'.format(i, minutes))

	f.close()
	g.close()

if __name__ == '__main__':
#	solve('B-sample')
	solve('B-small-attempt1')
#	solve('B-large')

