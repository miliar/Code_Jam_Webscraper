# 18:00 - 18:04 | 18:40

import math
import Queue
import copy

def solve(naomi, ken):
	naomi.sort()
	ken.sort()

	n = len(naomi)

	r = n - 1
	v1 = 0
	for x in xrange(n):
		if naomi[n-x-1] > ken[r]:
			v1 += 1
		else:
			r -= 1

	l = 0
	v2 = 0
	for x in xrange(len(naomi)):
		if naomi[x] > ken[l]:
			v2 += 1
			l += 1

	return v1, v2

def main():
	# fp = open('c.in')
	# fp = open('D-small-attempt0.in')
	fp = open('D-large.in')
	# fp = open('A-small-practice.in')
	# fp = open('A-large-practice.in')

	for case in xrange(int(fp.readline())):
		n = int(fp.readline())

		naomi = map(float, fp.readline().split())
		ken = map(float, fp.readline().split())

		result = solve(naomi, ken)

		print 'Case #{0}: {1} {2}'.format(case+1, result[1], result[0])

if __name__ == "__main__":
	main()
