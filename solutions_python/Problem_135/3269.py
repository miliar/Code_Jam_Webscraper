import sys, os

t = int(sys.stdin.readline())

for i in xrange(t):
	row1 = int(sys.stdin.readline())
	for j in xrange(4):
		if j + 1 == row1:
			row1Cards = sys.stdin.readline().strip().split()
		else: 
			curr = sys.stdin.readline()
	row2 = int(sys.stdin.readline())
	for j in xrange(4):
		if j + 1 == row2:
			row2Cards = sys.stdin.readline().strip().split()
		else: 
			curr = sys.stdin.readline()
	count = 0
	inCommon = ''
	for j in row1Cards:
		if j in row2Cards:
			count = count + 1
			inCommon = j
	if count == 0:
		print "Case #%d: " % (i+1) + "Volunteer cheated!"
	elif count == 1:
		print "Case #%d: " % (i+1) + inCommon
	else:
		print "Case #%d: " % (i+1) + "Bad magician!"