#!/usr/bin/env python
# to anyone who actually reads this, I'm so, so sorry.

import sys

def didwin(p,g):
	g = [l.replace('T',p) for l in g]
	if any(l == (p*4) for l in g): return True
	if all(g[n][n] == p for n in range(4)): return True
	if all(g[4-n-1][n] == p for n in range(4)): return True
	g= map("".join,zip(*g))
	if any(l == (p*4) for l in g): return True

for gamenum in range(1,int(sys.stdin.next())+1):
	sys.stdout.write("Case #%s: " %(gamenum,))
	game = map(str.strip, [sys.stdin.next(),sys.stdin.next(),sys.stdin.next(),sys.stdin.next()])
	sys.stdin.next()

	if didwin("X",game):
		print "X won"
	elif didwin("O",game):
		print "O won"
	elif not any("." in l for l in game):
		print "Draw"
	else:
		print "Game has not completed"
