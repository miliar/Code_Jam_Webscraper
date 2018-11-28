import sys
import re

f = open(sys.argv[1])

cases = int(f.readline())
for x in range(0, cases):

	values = [int(v) for v in f.readline().split(' ')]
	(a, b, k) = values

	winning = 0

	for aa in range(0, a):
		for bb in range(0, b):
			mult = aa & bb
			if mult < k:
				winning = winning + 1

	print 'Case #%d: %d' % (x+1, winning)
