# -*- coding: utf-8 *-*
from ContestSolver import ContestSolver


def solver(case):
	A, B, K = case[0]
	count = 0
	for a in range(A):
		for b in range(B):
			if a&b < K:
				count += 1
	return [count]


solution = ContestSolver(solver)
#solution.run("B-test", ints=True, test=True)
solution.run("B-small-attempt0", ints=True)
#solution.run("B-large", ints=True, watch=True)
