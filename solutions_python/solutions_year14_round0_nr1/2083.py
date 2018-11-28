import sys

def winnerForList(inList):
	listSum = sum(inList)
	if listSum == 13 or listSum == 4:
		return 1
	elif listSum == 7 or listSum == -4:
		return -1
	return 0


if __name__ == "__main__":
	f = sys.stdin
	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		if fn != '-':
			f = open(fn)

	t = int(f.readline())
	for _t in xrange(t):
		firstrow = int(f.readline())
		firstset = None
		for _r in xrange(4):
			row = set(f.readline().strip().split(' '))
			if _r == firstrow - 1:
				firstset = row
		secondrow = int(f.readline())
		secondset = None
		for _r in xrange(4):
			row = set(f.readline().strip().split(' '))
			if _r == secondrow - 1:
				secondset = row
		intersection = firstset.intersection(secondset)
		if len(intersection) == 1:
			print "Case #%d: %s" % (_t + 1, intersection.pop())
		elif len(intersection) == 0:
			print "Case #%d: Volunteer cheated!" % (_t + 1)
		else:
			print "Case #%d: Bad magician!" % (_t + 1)


		# if winner == 1:
		# 	print "Case #%d: X won" % (_t + 1)
		# elif winner == -1:
		# 	print "Case #%d: O won" % (_t + 1)
		# elif emptyfound:
		# 	print "Case #%d: Game has not completed" % (_t + 1)
		# else:
		# 	print "Case #%d: Draw" % (_t + 1)

		# # prepare to read next set
		# f.readline()