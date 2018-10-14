#!/usr/bin/python

import sys
import re
import networkx as nx

def verify_word(G, word):
	if '(' in word:
		print "verify_word shouldn't get ambigous words"
	for j in xrange(1, len(word) + 1):
		if word[:j] not in G[word[:j-1]]:
			return 0
	return 1
	
def v(G, word):
	m = re.search(r'\([a-z]*\)', word)
	if m:
		alt = m.group(0).strip("()")
		result = 0
		for c in alt:
			w = word[0:m.start()] + c + word[m.end():]
			ver_w = word[0:m.start()] + c
			if '(' in w:
				if verify_word(G, ver_w) != 0:
					result += v(G, w)
			else:
				result += verify_word(G, w)
		return result
	else:
			# No parentheses to resolve
			return verify_word(G, word)
	
(L, D, N) = map(int, sys.stdin.readline().strip().split(" "))
G = nx.DiGraph()
G.add_node("")
# words
for i in xrange(0, D):
	word = sys.stdin.readline().strip()
	for j in xrange(1, L + 1):
		G.add_node(word[:j])
		G.add_edge(word[:j-1], word[:j])
for i in xrange(0, N):
	case = sys.stdin.readline().strip()
	print "Case #%d: %d" % (i + 1, v(G, case))
