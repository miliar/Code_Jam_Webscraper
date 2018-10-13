import sys

T = int(sys.stdin.readline())

def make_tree(path, curdir):
	newdir = path.pop(0)
	if len(path) > 0:
		if newdir not in curdir:
			curdir[newdir] = {}
			return make_tree(path, curdir[newdir]) + 1
		else:
			return make_tree(path, curdir[newdir])
	else:
		if newdir not in curdir:
			curdir[newdir] = {}
			return 1
		else:
			return 0

for testcase in range(1, T+1):
	root = {}
	(N, M) = map(int, sys.stdin.readline().split())
	count = 0
	for n in range(N):
		path = sys.stdin.readline().strip().split('/')
		make_tree(path[1:], root)
	for m in range(M):
		path = sys.stdin.readline().strip().split('/')
		count += make_tree(path[1:], root)
	print('Case #%d: %d' % (testcase, count))
