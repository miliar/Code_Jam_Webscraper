import sys

data = [x.strip() for x in open(sys.argv[1])]

N = data.pop(0)

for t, test in enumerate(data):
	test = test.split(" ")
	C = int(test.pop(0))
	combine = {}
	for c in xrange(C):
		combination = test.pop(0)
		combine[combination[:2]] = combination[2]
		combine[combination[1]+combination[0]] = combination[2]
	D = int(test.pop(0))
	opposed = {}
	for d in xrange(D):
		opposing = test.pop(0)
		opposed[opposing[1]] = opposing[0]
		opposed[opposing[0]] = opposing[1]
	N = int(test.pop(0))
	invocation = test.pop(0)
	spell = ""
	bad = set()
	for element in invocation:
		spell += element
		if spell[-2:] in combine:
			while spell[-2:] in combine:
				spell = spell[:-2] + combine[spell[-2:]]
			bad = set()
			for element in spell:
				if element in opposed:
					bad.add(opposed[element])
		else:
			if element in bad:
				spell = ""
				bad = set()
			else:
				if element in opposed:
					bad.add(opposed[element])
	print "Case #%d: [%s]" % (t+1, ', '.join([x for x in spell]))