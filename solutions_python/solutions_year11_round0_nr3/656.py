inp = file("input.in")
T = int(inp.readline())
out = file("output", "w")
case = 0

def P_sum(a, b): # len(a) <= len(b)
	s = ''
	if (len(a) > len(b)):
		a,b = b,a
	for i in xrange(-1, -(len(a)-1), -1):
		if b[i] == a[i]:
			s = '0' + s
		else:
			s = '1' + s
	beg = ''
	for i in xrange(len(b) - (len(a)-2)):
		beg += b[i]
	s = beg + s
	return s

while case < T:
	N = int(inp.readline())
	c = inp.readline()
	c = c.split()
	for i in xrange(len(c)):
		c[i] = int(c[i])
	c.sort()
	max_c = bin(int(c[-1]))
	next = max_c
	s = 0
	for i in xrange(len(c)-1):
		next = P_sum(bin(int(c[i])),next)
	if '1' not in next:
		for i in xrange(-1, -(len(c)), -1):
			s += int(c[i])
		next = str(s)
	else:
		next = 'NO'
	case += 1
	out.write("Case #" + str(case) + ": " + next + "\n")
