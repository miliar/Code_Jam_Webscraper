
file = open("magicka.in")


def replaceComb(list, combs):
	if (len(list) > 1):
		for cmb in combs:
			if ((list[-1] == cmb[0] and list[-2] == cmb[1]) or (list[-1] == cmb[1] and list[-2] == cmb[0])):
				list.pop()
				list.pop()
				list.append(cmb[2])
				break;
	return list

def findOps(list, ops):
	if (len(list) > 1):
		for op in ops:
			for i in [0, 1]:
				other = (i + 1) % 2
				if (list[-1] == op[i]):
					for j in range(0, len(list) - 1):
						if (list[j] == op[other]):
							return []
	return list

caseNo = 1
file.readline()
for line in file:
	tokens = line.strip().split()

	ops = []
	combs = []

	index = 0
	noCmbs = int(tokens[0])

	while(index < noCmbs):
		index += 1
		combs.append(tokens[index])

	index += 1
	noOps = int(tokens[index])

	while(index < noCmbs + noOps + 1):
		index += 1
		ops.append(tokens[index])

	index += 1
	index += 1
	invocations = tokens[index]

	list = []

	for c in invocations:
		list.append(c)
		list = replaceComb(list, combs)
		list = findOps(list, ops)
	'''
	print "Case #%d: [" % caseNo,
	for l in range(0, len(list)):
		print "%c" % list[l],
		if (l != len(list) - 1):
			print ",",
	print "]"
	'''
	# remember to remove quotes from output
	print "Case #%d: %s" % (caseNo, list)
	caseNo += 1

