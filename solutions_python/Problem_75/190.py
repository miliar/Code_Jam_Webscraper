file = open("M.txt", "r").read(100000)

filename = "out.txt"

out = open(filename, 'w')

parts = file.split("\n")
n = int(parts.pop(0))

for i in range(1,n+1):
	line = parts.pop(0)
	fields = line.split(" ")
	a = int(fields[0])
	b = int(fields[a+1])
	c = int(fields[-2])
	aa = [fields[q] for q in range(1, 1+a)]
	bb = [fields[q] for q in range(2+a, 2+a+b)]
	cc = [fields[-1][q] for q in range(0, c)]
	stack = []
	for x in range(0, len(cc)):
		stack.append(cc[x])
		if len(stack) < 2:
			continue;
		for aaa in aa:
			if len(stack) >= 2 and ((stack[-1] == aaa[0] and stack[-2] == aaa[1]) or (stack[-2] == aaa[0] and stack[-1] == aaa[1])):
				stack.pop()
				stack.pop()
				stack.append(aaa[2])
		for bbb in bb:
			if bbb[0] in stack and bbb[1] in stack:
				stack = []
	out.write(("Case #%d: [%s]\n" % (i, ", ".join(map(str, stack)))))