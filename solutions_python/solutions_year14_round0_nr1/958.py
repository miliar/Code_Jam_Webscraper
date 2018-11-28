# -*- coding: utf-8 *-*
import ContestSolver as ContestSolver


def solver(case):
	row1 = case[case[0]]
	row2 = case[5 + case[5]]
	#print row1, row2
	intersect = [val for val in row1 if val in row2]
	#print intersect
	if len(intersect) == 0:
		return ["Volunteer cheated!"]
	elif len(intersect) > 1:
		return ["Bad magician!"]
	else:
		return [intersect[0]]

solution = ContestSolver.ContestSolver(solver)
#solution.run("A-test", ints=True, test=True)
solution.run("A-small-attempt0", ints=True)
#solution.run("A-large")
