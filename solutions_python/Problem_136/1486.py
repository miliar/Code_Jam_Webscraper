import sys
from decimal import Decimal


def solution(paths):
	global DEBUG
	if len(paths) < 2:
		return None
	current_sum = paths[-1][2] + paths[-1][3]
	last_sum = paths[-2][2] + paths[-2][3]
	if current_sum > last_sum:
		return last_sum
	return None


def solve(C, F, X):
	"""
	C = Farm Cost
	F = Farm Production
	X = Goal
	"""
	global DEBUG
	paths = [
		[2.0, C/2.0, X/2.0, 0],
	]
	i = 0
	while not solution(paths):
		paths.append([
			paths[-1][0]+F, 
			C/(paths[-1][0]+F),
			X/(paths[-1][0]+F),
			paths[-1][1] + paths[-1][3]
		])
	return solution(paths)

T = int(sys.stdin.readline())
for i in xrange(T):
	C, F, X = map(float, sys.stdin.readline().split(' '))
	print "Case #{0}: {1:.7f}".format(i+1, solve(C, F, X))