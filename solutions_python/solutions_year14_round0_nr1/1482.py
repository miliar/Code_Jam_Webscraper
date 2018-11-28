# 12:32

import math
import Queue
import copy

def solve():
	return 'result'

def main():
	# fp = open('a.in')
	fp = open('A-small-attempt1.in')

	for case in xrange(int(fp.readline())):
		cards1 = []
		cards2 = []

		v1 = int(fp.readline())

		for x in xrange(4):
			cards1.append(fp.readline().strip().split())

		v2 = int(fp.readline())

		for x in xrange(4):
			cards2.append(fp.readline().strip().split())

		r = set(cards1[v1-1]) & set(cards2[v2-1])

		if len(r) == 1:
			print 'Case #{0}: {1}'.format(case+1, r.pop())
		elif len(r) == 0:
			print 'Case #{0}: Volunteer cheated!'.format(case+1)
		else:
			print 'Case #{0}: Bad magician!'.format(case+1)

if __name__ == "__main__":
	main()
