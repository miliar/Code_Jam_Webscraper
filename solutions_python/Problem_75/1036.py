lines = open('./B-small-attempt0.in').readlines()[1:]
case = 0
for line in lines:
	case += 1
	
	items = line.split()
	items.reverse()

	if items.pop() == '1':
		combine = items.pop()
	else:
		combine = None

	if items.pop() == '1':
		opposed = items.pop()
	else:
		opposed = None

	items.pop()
	words = list(items.pop())

	# invoke
	words.reverse()	
	invokes = []
	while words:
		invokes.append(words.pop())

		if combine and len(invokes) >= 2:
			if (combine[0] in invokes[-2:]) and (combine[1] in invokes[-2:]):
				if (combine[0] == combine[1]):
					if (invokes[-2:].count(combine[0]) >= 2):
						invokes[-2:] = [combine[2]]
				else:
					invokes[-2:] = [combine[2]]

		if opposed and len(invokes) >= 2:
			if (opposed[0] in invokes) and (opposed[1] in invokes):
				if (opposed[0] == opposed[1]):
					if (invokes.count(opposed[0]) >= 2):
						invokes = []
				else:
					invokes = []

	print "Case #%d: [%s]" % (case, ", ".join(invokes))
