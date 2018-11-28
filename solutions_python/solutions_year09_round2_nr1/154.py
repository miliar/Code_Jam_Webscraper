import sys
import re

inp = sys.stdin.readline().strip().split()
N = int(inp[0])

def prob(weight, tree, features):
#	print "# prob(", weight, ",", tree, ",", features, ")"
	if not isinstance(tree, tuple):
		return weight * tree
	elif len(tree) > 1:
		if tree[1] in features:
			return prob(weight * tree[0], tree[2], features)
		else:
			return prob(weight * tree[0], tree[3], features)
	else:
		return weight * tree[0]

for n in xrange(N):
	print "Case #%d:" % (n + 1)
	inp = sys.stdin.readline().strip().split()
	K = int(inp[0])
	treestr = ""
	for k in xrange(K):
		treestr += " " + re.sub(r'\n', r' ', sys.stdin.readline().strip())
#	print "#1#", treestr
	treestr = re.sub(r'([a-z][a-z]*)', r'"\1"', treestr.strip())
#	print "#2#", treestr
	treestr = re.sub(r'\s\s*', r', ', treestr)
#	print "#3#", treestr
	#treestr = re.sub(r'[)]', r',)', treestr)
	treestr = re.sub(r'[(]\s*,', r'(', treestr)
#	print "#4#", treestr
	tree = eval(treestr)
#	print "#", tree
	inp = sys.stdin.readline().strip().split()
	A = int(inp[0])
	for a in xrange(A):
		inp = sys.stdin.readline().strip().split()
		print "%.7f" % prob(1.0, tree, inp[2:])

