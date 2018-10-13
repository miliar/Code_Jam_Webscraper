def compare(table1, table2):
	click = -1
	count = 0
	for val in table1:
		if val in table2:
			count += 1
			click = val
	return count, click		

import sys
with open('/users/nishanthshanmugham/Downloads/A-small-attempt1.in') as sys.stdin:

	T = int(sys.stdin.readline())

	for case_n in range(T):
		row1 = int(sys.stdin.readline())
		for skiplines in range(row1-1):
			sys.stdin.readline()
		row1elements = sys.stdin.readline().strip()
		table1 = row1elements.split(" ")

		for skiplines in range(4-row1):
			sys.stdin.readline()

		row2 = int(sys.stdin.readline())
		for skiplines in range(row2-1):
			sys.stdin.readline()
		row2elements = sys.stdin.readline().strip()
		table2 = row2elements.split(" ")

		tup = compare(table1, table2)
		if tup[0] == 1:
			print "Case #%d: %d" % (case_n+1, int(tup[1]))
		elif (tup[0] > 1):
			print "Case #%d: Bad magician!" % (case_n+1)
		else:
			print "Case #%d: Volunteer cheated!" % (case_n+1)

		for skiplines in range(4-row2+1-1):
			sys.stdin.readline()
