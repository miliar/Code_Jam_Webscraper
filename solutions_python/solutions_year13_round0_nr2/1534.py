def checklawn(lawn):
	# if there is a block of grass which is neither tallest in it's row nor in it's column
	# it can't be cut using the lawn mower
	n = len(lawn)
	m = len(lawn[0])
	rowMax = []
	columnMax = []
	for r in lawn : # row
		rowMax.append(max(r))
	for j in range(m) : # column
		column = [row[j] for row in lawn]
		columnMax.append(max(column))

	for i in range(n) :
		for j in range(m) :
			if lawn[i][j] < rowMax[i] and lawn[i][j] < columnMax[j] :
				return False

	return True

# it starts here
import sys
l = sys.stdin.readline()
count = int(l)

results = []
for i in range(count) :
	n,m = sys.stdin.readline().split()
	n = int(n)
	m = int(m)
	lawn = []
	for j in range(n) :
		line = sys.stdin.readline().rstrip().split()
		lawn.append(line)

	r = checklawn(lawn)
	results.append(r)

# print results
for i in range(count):
	msg = 'YES' if results[i] else 'NO'
	print 'Case #' + str(i+1) + ": " + msg
