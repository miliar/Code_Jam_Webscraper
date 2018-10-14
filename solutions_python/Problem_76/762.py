import operator

inp = open('C-large.in')
out = open('out.txt', 'wt')

cases = int(inp.readline())
for case in range(1, cases+1):
	_ = inp.readline()
	line = [int(i) for i in inp.readline().split()]

	if reduce(operator.xor, line) == 0:
		m = min(line)
		line.pop(line.index(m))
		result = sum(line)
	else:
		result = "NO"


	print "Case #%d: %s" % (case, result)
	out.write("Case #%d: %s\n" % (case, result))

out.close()
