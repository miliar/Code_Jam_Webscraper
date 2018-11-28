infile = open("B-large.in")
outfile = open("b.out",'w')
T = int(infile.readline())
for i in range(T):
	N,M = map(int,infile.readline().split(' '))
	field = []
	for j in range(N):
		field.append(map(int,infile.readline().split(' ')))
	
	#Check each position in the field to see if the square is possible
	possible = True
	for x in range(N):
		for y in range(M):
			#check the left to right
			horizontal = True
			here = field[x][y]
			for p in range(M):
				#print x,p
				if field[x][p] > here:
					#print x,p
					horizontal = False
					break
			#print 
			#check top to bottom
			vertical = True
			for p in range(N):
				if field[p][y] > here:
					vertical = False
					break
			if not horizontal and not vertical:
				possible = False
				break
		if not possible:
			break
	if possible:
		line =  "Case #%d: YES\n"%(i+1)
		outfile.write(line)
	else:
		line = "Case #%d: NO\n"%(i+1)
		outfile.write(line)