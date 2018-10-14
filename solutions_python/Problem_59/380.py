"""
python 2.6.x program by Ji Han
"""

import sys

def mknode(parent, name):
	if not name in parent:
		parent[name] = dict()
		return 1
	return 0

def main():
	T = int(sys.stdin.readline())
	for k in range(1, T + 1):
		line = sys.stdin.readline()
		N, M = map(int, line.split())
		root = dict()
		count = 0
		for p in range(N):
			line = sys.stdin.readline().rstrip() # god-damned trailing '\n'
			L = line.split('/')  # oops..my os.path.sep isn't '/'
			pivot = root
			for i in range(1, len(L)):  # L[0] is ''
				trunk = L[i]
				mknode(pivot, trunk)
				pivot = pivot[trunk]
		for p in range(M):
			line = sys.stdin.readline().rstrip()
			L = line.split('/')
			pivot = root
			for i in range(1, len(L)):  # ditto
				trunk = L[i]
				count = count + mknode(pivot, trunk)
				pivot = pivot[trunk]
		print "Case #%d: %d" % (k, count)

if __name__=='__main__': 
        main()

