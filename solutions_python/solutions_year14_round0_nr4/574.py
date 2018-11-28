import sys

data = sys.stdin.readlines()
counter = 0
numTests = int(data[counter])
counter += 1

for i in xrange(numTests):
	n = int(data[counter])
	counter += 1
	nRow = map(float, data[counter].split())
	counter += 1
	kRow = map(float, data[counter].split())
	counter += 1

	nRow.sort()
	kRow.sort()
	nRow.reverse()
	kRow.reverse()

	kRowCopy = list(kRow)

	for val in nRow:
		for val2 in kRowCopy:
			if val > val2:
				kRowCopy.remove(val2)
				break

	valOfDeceitWar =  n - len(kRowCopy)

	score = 0

	for val in nRow:
		l = filter(lambda y : y != False, \
			map(lambda x : x if x > val else False, kRow))

		if len(l) == 0:
			kRow = kRow[:len(kRow) - 1]
			score += 1
			
		else:
			kRow.remove(min(l))

	print "Case #" + str(i+1) + ": " + str(valOfDeceitWar) + " " + str(score)
