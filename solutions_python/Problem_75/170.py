import sys

def tokens(line):
	tokens = line.split()
	for token in tokens:
		yield token
		
def solve(tokens):
	combine = {}
	oppose = {}

	C = int(tokens.next())
	for c in xrange(C):
		comb = tokens.next()
		combine[comb[0] + comb[1]] = comb[2]
		combine[comb[1] + comb[0]] = comb[2]
		
	D = int(tokens.next())
	for d in xrange(D):
		opp = tokens.next()

		if opp[0] in oppose:
			oppose[opp[0]].append(opp[1])
		else:
			oppose[opp[0]] = [ opp[1] ]

		if opp[1] in oppose:
			oppose[opp[1]].append(opp[0])
		else:
			oppose[opp[1]] = [ opp[0] ]
	
	N = int(tokens.next())
	invoke = tokens.next()
	
	cast = ''
	for i in invoke:
		cast += i
		
		while True:
			pair = cast[-2:]
			if pair in combine:
				cast = cast[:-2] + combine[pair]
			else:
				break
				
		last = cast[-1]
		if last in oppose:
			for opp in oppose[last]:
				if opp in cast:
					cast = ''
					break
	
	return '[' + ', '.join([c for c in cast]) + ']'

with open(sys.argv[1]) as f:
	T = int(f.readline())
	for testcase in xrange(T):
		answer = solve(tokens(f.readline()))
		print 'Case #%d: %s' % (testcase + 1, answer) 