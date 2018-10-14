from os.path import *

def y(dirs0, dirs1):
	root = {}
	for path in dirs0:
		node = root
		for dir in path.split('/'):
			if dir in node:
				pass
			else:
				node[dir] = {}
			node = node[dir]
	###
	n = 0
	for path in dirs1:
		node = root
		for dir in path.split('/'):
			if dir in node:
				pass
			else:
				node[dir] = {}
				n += 1
			node = node[dir]
	return n

T = int(raw_input())
for x in xrange(1, T + 1):
	N, M = map(int, raw_input().split(' '))
	dirs0 = [raw_input()[1:] for _ in xrange(N)]
	dirs1 = [raw_input()[1:] for _ in xrange(M)]
	print('Case #%d: %d' % (x, y(dirs0, dirs1)))
