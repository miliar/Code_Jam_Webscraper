import sys
#sys.stdin = open ('B-small.in')
#sys.stdout = open ('B-small.out', 'w')

T = input ()
for i in xrange (T):
	data = raw_input ().split ()
	c = int (data[0])
	combined = data[1:1 + c]
	d = int (data[c + 1])
	opposed = data[c + 2:c + 2 + d]
	n = int (data[c + d + 2])
	invoked = data[-1]
	cur = []
	for elem in invoked:
		ok = False
		if len (cur) > 0:
			for s in combined:
				if cur[-1] == s[0] and elem == s[1] or cur[-1] == s[1] and elem == s[0]:
					cur[-1] = s[2]
					ok = True
					break
		if not ok:
			for s in opposed:
				if (elem == s[0]) and (s[1] in cur) or (elem == s[1]) and (s[0] in cur):
					cur = []
					ok = True
		if not ok:
			cur.append (elem)
	print 'Case #{}: {}'.format (i + 1, '[' + ', '.join (cur) + ']')
