import csv
with open('A-small-attempt0.in', 'rb') as trick:
	table = csv.reader(trick, delimiter=' ')
	tests = int(table.next()[0])
	for t in xrange(tests):
		first = int(table.next()[0])
		frows = [table.next(), table.next(), table.next(), table.next()]
		second = int(table.next()[0])
		srows = [table.next(), table.next(), table.next(), table.next()]
		result = list(set(frows[first-1]) & set(srows[second-1]))
		if len(result) == 1:
			print "Case #" + str(t+1) + ": " + str(result[0])
		elif len(result) == 0:
			print "Case #" + str(t+1) + ": Volunteer cheated!"
		else:
			print "Case #" + str(t+1) + ": Bad magician!"