import sys
import re

(L, D, N) = map(int, sys.stdin.readline().split(' '))

words = []
for word in range(D):
	words.append(sys.stdin.readline().strip())

for case in range(N):
	print "Case #%d:" % (case + 1),
	p = False
	pats = []
	pl = set()
	for i in sys.stdin.readline().strip():
		if i == '(':
			p = True
		elif i == ')':
			p = False
		else:
			pl.add(i)
		if not p:
			pats.append(pl)
			pl = set()
	matching = words
	for p in range(L):
		matching = filter(lambda x: x[p] in pats[p], matching)
		if len(matching) == 0:
			break
	print len(matching)
			
	