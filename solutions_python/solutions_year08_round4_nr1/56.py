#!/usr/bin/env python
import sys

def both(a, b):
	if a == -1 or b == -1:
		return -1
	else:
		return a + b;

def least(a, b):
	if a == -1:
		return b
	elif b == -1:
		return a
	else:
		return min(a, b)

argv = sys.argv[1:]

inFile = open(argv[0] + '.in', 'rb')
outFile = open(argv[0] + '.out', 'wb')

n = int(inFile.readline())
for i in xrange(n):
	m,v = map(int, inFile.readline().split())
	nodes = [0]
	for j in xrange(m):
		nodes.append(map(int, inFile.readline().split()))
		print 'Node %i: %s' % (j + 1, ' '.join(map(str, nodes[-1])))
	cheats = [0]*(m + 1)
	
	for j in xrange(m, 0, -1):
		node = nodes[j]
		cheat = [-1, -1]
		if len(node) == 2:
			lCheat = cheats[2*j]
			rCheat = cheats[2*j + 1]
			
			or0 = both(lCheat[0], rCheat[0])
			or1 = least(lCheat[1], rCheat[1])
			and0 = least(lCheat[0], rCheat[0])
			and1 = both(lCheat[1], rCheat[1])
			
			if node[0]:
				or0 = both(or0, 2*node[1] - 1)
				or1 = both(or1, 2*node[1] - 1)
			else:
				and0 = both(and0, 2*node[1] - 1)
				and1 = both(and1, 2*node[1] - 1)
			
			cheat = [least(or0, and0), least(or1, and1)]
		else:
			cheat = [-node[0], node[0] - 1]
		print 'cheats[%i] = %s' % (j, cheat)
		cheats[j] = cheat
	
	if cheats[1][v] == -1:
		print 'Case #%i: IMPOSSIBLE' % (i + 1)
		outFile.write('Case #%i: IMPOSSIBLE\n' % (i + 1))
	else:
		print 'Case #%i: %i' % (i + 1, cheats[1][v])
		outFile.write('Case #%i: %i\n' % (i + 1, cheats[1][v]))

outFile.close()
inFile.close()

