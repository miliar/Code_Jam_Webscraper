file = open("sean.in")

lineIndex = 0
caseNo = 1
file.readline()
for line in file:
	lineIndex += 1
	if (lineIndex % 2 == 1):
		continue

	tokens = line.strip().split()
	numbers = []
	for s in tokens:
		numbers.append(int(s))

	numbers.sort()

	xor = 0
	sum = 0
	for n in numbers:
		xor ^= n
		sum += n

	if (xor != 0):
		print "Case #%d: NO" % caseNo
	else:
		print "Case #%d: %d" % (caseNo, sum - numbers[0])
	caseNo += 1
