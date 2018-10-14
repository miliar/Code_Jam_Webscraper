from sys import stdin

def get_int_arr():
	return [int(x) for x in stdin.readline().split(' ')]

count = 0
def addpath(root, path):
	global count
	tree = path[1:].split('/')
	ptr = root
	for name in tree:
		if not ptr.has_key(name):
			count += 1
			ptr[name] = {}
		ptr = ptr[name]

def solve():
	global count
	N, M = get_int_arr()
	

	fsys = {'/':{}}
	for i in range(N):
		addpath(fsys, stdin.readline().strip())
	count = 0
	for i in range(M):
		addpath(fsys, stdin.readline().strip())
	print count


T = int(stdin.readline())
for case in range(T):
	print 'Case #%d:' % (case+1),
	solve()
