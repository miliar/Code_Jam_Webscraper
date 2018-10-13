# coding: shift-jis

import sys

f = file(sys.argv[1])

test_cnt = int(f.readline())

for case in range(1, test_cnt+1):
	V, H = map(int, f.readline().split())
	row = [list(f.readline()[:-1]) for _ in range(V) ] 
	
	ret = True
	for v in range(V):
		for h in range(H):
			if row[v][h] == '#':
				if v == V-1 or h == H-1:
					ret = False
					break
				if row[v][h+1] != '#' or row[v+1][h] != '#' or row[v+1][h+1]!='#':
					ret = False
					break
				
				row[v][h]     = '/'
				row[v][h+1]   = '\\'
				row[v+1][h]   = '\\'
				row[v+1][h+1] = '/'
					
	
	print 'Case #%d:'%case
	if ret:
		for r in row:
			print reduce(lambda a,b:a+b, r)
	else:
		print 'Impossible'
