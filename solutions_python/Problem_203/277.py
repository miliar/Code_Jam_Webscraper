number = raw_input()

def parseInput(example):
	stripped_example = example.strip()
	l = stripped_example.split(" ")
	return(int(l[0]), int(l[1]))

def printMap(m, R, C):
	for row in m:
		print(''.join(row))

def solve(m, R, C):
	for r in xrange(R):
		current = '?'
		for c in xrange(C):
			if m[r][c] != '?':

				if current == '?':
					for lc in xrange(c):
						m[r][lc] = m[r][c]

				current = m[r][c]
			m[r][c] = current
	for c in xrange(C):
		current = '?'
		for r in xrange(R):
			if m[r][c] != '?':

				if current == '?':
					for lr in xrange(r):
						m[lr][c] = m[r][c]

				current = m[r][c]
			m[r][c] = current
	printMap(m, R, C)

for n in xrange(int(number)):
	example = raw_input()
	(R, C) = parseInput(example)
	m = []
	for r in xrange(R):
		row = raw_input()
		m.append(list(row))
	
	print "Case #" + str(n + 1) +":"	
	solve(m, R, C)
	#print "Case #" + str(n + 1) +": " + str(solve(example))