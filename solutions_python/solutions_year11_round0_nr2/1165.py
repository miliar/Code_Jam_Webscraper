from collections import defaultdict

T = int(raw_input())
for i in xrange(T):
	line = raw_input().split()
###	print line
	C = int(line.pop(0))
	
	products = {}	
	for j in xrange(C): # combinations
		base1, base2, product = list(line.pop(0))

		b1,b2 = sorted([base1,base2])
		products[(b1,b2)] = product
	
	D = int(line.pop(0))
	opposites = defaultdict(set)
	for j in xrange(D):
		base1, base2 = list(line.pop(0))
		b1, b2 = sorted([base1, base2])
		opposites[b1].add(b2)
		opposites[b2].add(b1)
	N = int(line.pop(0))
	sequence = line.pop(0)

	stack = []
	idx = defaultdict(int)
	for element in sequence:
		if len(stack):
			previous = stack[-1]
			b1, b2 = sorted([element, previous])

			# check for combinations
			if (b1,b2) in products:
				p = products[(b1,b2)]
				idx[stack.pop()] -= 1
				stack.append(p)
				idx[p] += 1
			else:
				stack.append(element)
				idx[element] += 1

			previous = stack[-1]
			# check for oppositions
			for e in idx:
				if idx[e] and e in opposites[previous]:
###					print e, "clears", previous
					stack = []
					idx = defaultdict(int)

		else:
			stack.append(element)
			idx[element] = 1
###		print stack
###		print idx

	print "Case #%d: [%s]" % (i + 1, ", ".join(c for c in stack))

