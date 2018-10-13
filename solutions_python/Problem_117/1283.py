import sys

# problem B from codejam qualification round

DEBUG = False

def can_mown(lawn):
	# find maximum values in rows
	max_rows = [max(row) for row in lawn]
	# find max values in columns
	max_cols = []
	for i in xrange(len(lawn[0])):
		max_cols.append(max([row[i] for row in lawn]))
	if DEBUG:
		print max_rows
		print max_cols
	# now check each square
	can = True
	for i, row in enumerate(lawn):
		for j, square in enumerate(row):
		# square should be the maximal value eitherin the row on in the column
			if square < max_rows[i] and square < max_cols[j]:
				can = False
				break
	if can:
		return "YES"
	else:
		return "NO"


def main():
	f = sys.stdin
	T = int(f.readline().strip())
	
	for case in xrange(1, T + 1):
		N, M = [int(x) for x in f.readline().split()][:2]
		lawn = []
		for i in xrange(N):
			lawn.append([int(x) for x in f.readline().split()])
		if DEBUG:
			print lawn
			print ""
		
		print "Case #%d: %s" % (case, can_mown(lawn))
				
if __name__ == "__main__":
	main()