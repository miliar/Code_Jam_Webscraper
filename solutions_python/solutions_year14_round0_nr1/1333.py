import os, sys
import itertools
lines = [line.strip() for line in open("%s" % sys.argv[1]).readlines()]
lines.reverse()
cases = lines.pop()
for case in range(int(cases)):
	print "Case #%s:" % (case + 1),
	row1 = int(lines.pop()) - 1
	grid1 = [lines.pop().split(' ') for i in range(4)]
	row2 = int(lines.pop()) - 1
	grid2 = [lines.pop().split(' ') for i in range(4)]
	cards = set(grid1[row1]).intersection(grid2[row2])
	if len(cards) == 0:
		print "Volunteer cheated!"
	elif len(cards) == 1:
		print list(cards)[0]
	else:
		print "Bad magician!"

	
	
