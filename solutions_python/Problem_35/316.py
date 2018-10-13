#!/usr/bin/python

import sys, string, itertools

def getl():
	return sys.stdin.readline().rstrip()

def mark_sinks(a):
	for row in range(h):
		for col in range(w):
			cell = int(a[row][col][1:])
			first = not (row > 0 and int(a[row-1][col][1:]) < cell)
			second = not (row < h-1 and int(a[row+1][col][1:]) < cell)
			third = not (col > 0 and int(a[row][col-1][1:]) < cell)
			fourth = not (col < w-1 and int(a[row][col+1][1:]) < cell)
			if first and second and third and fourth: 
				sinks[row, col] = string.ascii_uppercase[len(sinks)]
				#a[row][col] = sinks[row, col]
	for s in sinks.keys():
		a[s[0]][s[1]] = sinks[s] + a[s[0]][s[1]][1:]

def mark(a, x, y, history=None):
	if not history:
		history = []
	if a[x][y][0] != '?':
		for point in history:
			a[point[0]][point[1]] = a[point[0]][point[1]].replace('?', a[x][y][0], 1)
		#print('history:', history)
	else:
		history.append((x,y))
		# north west east south
		#print x, y
		values = [a[x-1][y] if x>0 else '!', 
				a[x][y-1] if y>0 else '!', 
				a[x][y+1] if y<w-1 else '!', 
				a[x+1][y] if x<h-1 else '!']
		dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
		min = 10001
		dir = 0
		for i in range(len(values)):
			#print 'values[i]: ', values[i]
			if values[i] == '!':
				continue
			value = int(values[i][1:])
			if value < min:
				min = value
				dir = i
		mark(a, x + dirs[dir][0], y + dirs[dir][1], history)

t = int(getl())

for i in range(t):
	h, w = [int(x) for x in getl().split()]
	m = []
	sinks = {}
	for j in range(h):
		r = ['?' + x for x in getl().split()]
		m.append(r)
	mark_sinks(m)
	for x in range(h):
		for y in range(w):
			if m[x][y][0] == '?':
				mark(m, x, y)
				#print(m)
	basins = 0
	mapping = {}
	#for element in itertools.chain(m):
	flag = False
	for row in m:
		for element in row:
			if element[0] not in mapping.keys():
				mapping[element[0]] = string.ascii_lowercase[basins]
				basins += 1
			if basins == len(sinks):
				flag = True
				break
		if flag:
			break
	#print(mapping)
	print('Case #{0}:'.format(i+1))
	for row in m:
		for ei in range(len(row))[:-1]:
			sys.stdout.write(mapping[row[ei][0]] + ' ')
		sys.stdout.write(mapping[row[-1][0]])
		print
