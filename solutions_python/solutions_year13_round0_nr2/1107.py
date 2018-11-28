#!/usr/bin/env python
import sys

f = open(sys.argv[1]).readlines()
count = 0
data = []
totalCases = f[0]
f.pop(0)

while f != []:
	#print f
	x,y = f[0].split()
	f.pop(0)
	d = []
	for i in range(int(x)):
		row = []
		for j in f[0].strip().split(" "):
			row.append(int(j))
		d.append(row)
		f.pop(0)
	data.append(d)

case = 1

#Code starts here
f = open(sys.argv[1]+".out", "w")
for d in data:
	print "==================="
	print d
	rows = len(d)
	cols = len(d[0])
	map = []
	for a in range(rows):
		row = []
		for b in range(cols):
			row.append(100)
		map.append(row)
	#print rows, cols
	# Mow horizontally
	for a in range(rows):
		highest = max(d[a])
		for b in range(cols):
			if map[a][b] > highest:
				map[a][b] = highest
	# Mow vertically
	for a in range(cols):
		col = []
		for b in range(rows):
			#print "*",a,b
			col.append(d[b][a])
		highest = max(col)
		for b in range(rows):
			if map[b][a] > highest:
				map[b][a] = highest
	print map
	if d == map:
		ans = "YES"
	else:
		ans = "NO"
	lineOut = "Case #"+str(case)+": "+ans
	print lineOut
	f.write(lineOut+"\n")
	case += 1
f.close()
