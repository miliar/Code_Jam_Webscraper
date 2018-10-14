
N = int(raw_input())


for no in range(1, N+1):
	res = 0
	cells = set([])
	
	for r in range(0, int(raw_input())): # R
		x1, y1, x2, y2 = tuple(map(int, raw_input().split()))
		for i in range(x1, x2+1):
			for j in range(y1, y2+1):
				cells.add((i,j))
	
	nbtour = 0
	while cells:
		ncells = set([])
				
		for i,j in cells:
			if (i+1, j-1) in cells:
				ncells.add((i+1, j))
		
		for i,j in cells:
			# tuerie d'une cell
			if (i-1, j) not in cells and (i, j-1) not in cells:
				pass
			else:
				# on garde l'ancienne
				ncells.add((i,j))
			
		
		nbtour += 1
		cells = ncells
	
	print 'Case #%d: %d' % (no, nbtour)
	
	