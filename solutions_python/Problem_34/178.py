import re

l, d, n = [int(s) for s in raw_input().split(' ')]
words = [raw_input() for i in xrange(d)]

for case in xrange(n):
	pattern = raw_input()
	parts = []
	tmp = None
	for c in pattern:
		if c == '(':
			tmp = []
			parts.append('(')
		elif c == ')':
			parts.append('|'.join(tmp))
			parts.append(')')
			tmp = None
		elif tmp is not None:
			tmp.append(c)
		else:
			parts.append(c)
	reg = ''.join(parts)
	prog = re.compile(reg)
	result = 0
	for w in words:
		if prog.match(w):
			result += 1
	
	print "Case #%d:"%(case+1), result