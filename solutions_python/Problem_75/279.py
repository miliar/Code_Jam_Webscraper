import sys

def buildC(rules):
	res = {}
	for rule in rules:
		res[rule[:2]] = rule[2]
		res[rule[1]+rule[0]] = rule[2]
	return res

def buildD(rules):
	res = {}
	for rule in rules:
		if rule[0] in res:
			res[ rule[0] ].add( rule[1] )
		else:
			res[ rule[0] ] = set([ rule[1] ])
		
		if rule[1] in res:
			res[ rule[1] ].add( rule[0] )
		else:
			res[ rule[1] ] = set([ rule[0] ])
	return res

def process(spell, C, D):
	stack = []
	for c in spell:
		if len(stack) == 0:
			stack.append(c)
		elif (c+stack[-1]) in C:
			stack[-1] = C[ c + stack[-1] ]
		elif c in D and not D[c].isdisjoint( set(stack) ):
			stack = []
		else:
			stack.append(c)
	return stack

fpath = sys.argv[1] if len(sys.argv) > 1 else "C:\projects\codejam\magicka.in"
f = open(fpath, 'r')
T = int(f.readline())
for tc in xrange(1,T+1):
	line = f.readline().split()
	
	Cno = int(line[0])
	C = buildC( line[1:Cno+1] )
	
	Dno = int( line[Cno+1] )
	D = buildD( line[Cno+2: Cno+2+Dno] )
	
	N = line[Cno+2+Dno]
	spell = line[Cno+2+Dno+1]
	
	#print "C={0}, D={1}, spell={2}".format(C, D, spell)
	res = process(spell, C, D)
	print "Case #{0}: {1}".format(tc, res).replace("'", "")
f.close()
