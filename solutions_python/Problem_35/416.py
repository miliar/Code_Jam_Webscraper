from copy import deepcopy
inp = open('B-large.in', 'r')
out = open('B.out', 'w')
n = int(inp.readline())

for k in range(n):
	x, y = map(int, inp.readline().split(' '))

	counter = 0
	
	tab = []
	res = [[0 for i in range(y)] for j in range(x)]
	
	def traverse(a, b):
		global counter, tab, res, x, y
		if res[a][b] != 0:
			return res[a][b]

		mini = tab[a][b]
		coords = False

		for ax, ay in ((a-1, b), (a, b-1), (a, b+1), (a+1, b)):
			if ax >= 0 and ax < x and ay >= 0 and ay < y:
				if tab[ax][ay] < mini:
					mini = tab[ax][ay]
					coords = (ax, ay)
		# print (a, b)[::-1], '->', coords and coords[::-1] or coords, 
		# if coords: 
		#  	print '(%d)'%tab[coords[0]][coords[1]]
		# else: print ''
			
		if not coords:
			counter += 1

			res[a][b] = counter
			return counter

		else:
			num = traverse(*coords)
			res[a][b] = num
			return num
	
	
	for i in range(x):
		tab.append(map(int, inp.readline().split(' ')))
		
	for a in range(x):
		for b in range(y):
			traverse(a, b)
			
	print >> out, "Case #%d:"%(k+1,)
	
	letters = [False for i in range(27)]
	letter = 0
	for a in range(x):
		for b in range(y):
			if not letters[res[a][b]]:				
				letters[res[a][b]] = chr(ord('a') + letter)
				letter += 1				
			print >> out, letters[res[a][b]],
			
		print >> out, ''
