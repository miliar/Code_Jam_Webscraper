inp = open('B-large.in')
out = open('out.txt', 'wt')

cases = int(inp.readline())
for case in range(1, cases+1):
	line = inp.readline().split()
	c = int(line[0])
	d = int(line[1+c])

	string = line[-1]
	conflict = {}
	combine = {}
	#print c, line[1:1+c], d, line[1+c+1:1+c+1+d], string
	for comb in line[1:1+c]:
		combine[comb[:2]] = comb[-1]
		combine[comb[:2:-1]] = comb[-1]
	for conf in line[1+c+1:1+c+1+d]:
		conflict[conf] = True
		conflict[conf[::-1]] = True

	stack = []
	for char in string:
		if not stack:
			stack.append(char)
			continue
		if combine.has_key(stack[-1] + char):
			sym = combine[stack[-1] + char]
			stack.pop()
			stack.append(sym)
			continue
		if combine.has_key(char + stack[-1]):
			sym = combine[char + stack[-1]]
			stack.pop()
			stack.append(sym)
			continue

		for item in stack:
			if conflict.has_key(item + char):
				stack = []
				break
			if conflict.has_key(char + item):
				stack = []
				break
		else:
			stack.append(char)

	print "Case #%d: [%s]" % (case, ", ".join(stack))
	out.write("Case #%d: [%s]\n" % (case, ", ".join(stack)))

out.close()
