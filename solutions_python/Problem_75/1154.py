T = int(raw_input())

for t in range(1, T+1):
	forms = {}
	opposed = []
	elements = []
	tokens = raw_input().split()

	C = int(tokens.pop(0))
	for _ in range(C):
		c = tokens.pop(0)
		forms[tuple(sorted(c[:2]))] = c[2]

	D = int(tokens.pop(0))
	for _ in range(D):
		d = tokens.pop(0)
		opposed += [tuple(sorted(d))]

	N = int(tokens.pop(0))
	n = tokens.pop(0)
	assert len(n) == N

	for char in n:
		elements += [char]
		if len(elements) < 2:
			continue
		form = forms.get(tuple(sorted(elements[-2:])))
		if form:
			elements = elements[:-2] + [form]
			continue
		for elem in set(elements):
			if tuple(sorted((char, elem))) in opposed:
				elements = []
				break

	print "Case #%d: [%s]" % (t, ', '.join(elements))
