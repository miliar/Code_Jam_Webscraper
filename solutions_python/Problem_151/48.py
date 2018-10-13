#!/usr/bin/env python
import itertools

t = input()

def node_count(www):
	#print 'node_count', s
	if not www: return 0
	trie = set()
	for w in www:
		for i in range(len(w)+1):
			trie.add(w[:i])
	#print trie
	return len(trie)

for ti in range(1, t+1):
	n, m = map(int, raw_input().split())
	s = map(lambda x: raw_input(), range(n))
	#print n, m, s

	ans, anscnt = 0, 0
	for ass in itertools.product(range(m), repeat=n):
		assignment = [[] for _ in range(m)]
		for i in range(n):
			assignment[ass[i]].append(s[i])
		#print 'assing', assignment
		val = sum(map(node_count, assignment))
		#print val
		if val > ans:
			ans, anscnt = val, 1
		elif val == ans:
			anscnt += 1

	
	print 'Case #' + str(ti) + ':', ans, anscnt