#!/usr/bin/python -d
import sys, string

alp=string.ascii_letters

lines = open(sys.argv[1]).readlines()

m = lines[0].strip()

def createMap(i, h):
	map = []
	for j in range(0, h):
		#map.append(lines[i+j+1])
		t = []
		for s in lines[i+j+1].split():
			t.append(int(s))
		map.append(t)
	return map

x = 1

def findSmallest(map, i, j):
	r=11000
	x,y = (-1,-1)

	try:
		a, b = i-1, j
		if (map[a][b]<map[i][j]) and (map[a][b]<r) and (a >=0) and (b >= 0):
			r = map[a][b]
			x,y = a,b
	except: pass    
	try:
		a, b = i, j-1
		if (map[a][b]<map[i][j]) and (map[a][b]<r) and (a >=0) and (b >= 0):
			r = map[a][b]
			x,y = a,b
	except: pass
	try:
		a, b = i, j+1
		if (map[a][b]<map[i][j]) and (map[a][b]<r) and (a >=0) and (b >= 0):
			r = map[a][b]
			x,y = a,b
	except: pass
	try:
		a, b = i+1, j
		if (map[a][b]<map[i][j]) and (map[a][b]<r) and (a >=0) and (b >= 0):
			r = map[a][b]
			x,y = a,b
	except: pass



	return x,y

def printOutput(case, mapX):
	print "Case #%d:" % (case)
	for a in mapX:
		for b in a:
			sys.stdout.write(str(b) + ' ')
		print ""

def createXX(map, h, w):
	a=-1
	mapX=[ ['' for i in range(w)] for i in range(h) ]
	for i in range(h):
		for j in range(w):
			if mapX[i][j] != "": continue

			path = []
			path.append([i,j])
			sa, sb = findSmallest(map, i, j)

			while(1 == 1):
				if (sa == -1): break
				path.append([sa,sb])
				sa, sb = findSmallest(map, sa, sb)

			z = ""
			for x in path:
				if mapX[x[0]][x[1]] != "": z = mapX[x[0]][x[1]]
		
			if z == "": 
				a += 1
				z = alp[a]
			
			for x in path:
				mapX[x[0]][x[1]] = z
			
	return mapX
	
case = 0
while(1==1):
	h = int(lines[x].split()[0])
	w = int(lines[x].split()[1])
	map=createMap(x, h)
	mapY=createXX(map, h, w)
	x = x+h+1
	case += 1
	#print mapY
	#print mapY
	#if (case == m): break
	#case += 1
	printOutput(case, mapY)

