from bisect import bisect_left
from collections import deque

def solve_optimal(naomi, ken, n):
	points = 0
	for i in xrange(n):
		if naomi[n-1-points] > ken[n-1-i]:
			points += 1

	return points

def solve_war(naomi, ken, n):
	points = 0
	p = 0
	for i in naomi:
		lowest = bisect_left(ken, i, lo=p)
		points += lowest - p
		p = lowest + 1
		if p == n:
			break

	return points		

tests = int(raw_input())

for test in xrange(1, tests+1):
	n = int(raw_input())
	naomi = sorted(map(float, raw_input().split()))
	ken = sorted(map(float, raw_input().split()))
	optimal = solve_optimal(naomi, ken, n)
	war = solve_war(naomi, ken, n)

	print 'Case #%s: %s %s' % (test, optimal, war)