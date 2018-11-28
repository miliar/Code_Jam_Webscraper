import sys
from fractions import gcd

def add_path(tree, path):
	res = 0 # number of mkdir ops
	dirs = path.split('/')[1:]
	for dir in dirs:
		if not dir in tree:
			res += 1
			tree[dir] = {}
		tree = tree[dir]
	return res


with open(sys.argv[1]) as f:
	T = int(f.readline())
	for tc in xrange(1, T+1):
		tree = {} #name -> tree
		N, M = map(int, f.readline().split())
		res = 0
		for n in range(N):
			path = f.readline().strip()
			add_path(tree, path)
		for m in range(M):
			path = f.readline().strip()
			res += add_path(tree, path)
		
		print "Case #{0}: {1}".format(tc, res)
#		print tree
