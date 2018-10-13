def solve():
	t = int(raw_input())
	for case in xrange(1,t+1):
		rows,cols = map(int,raw_input().split())
		pict = []
		for r in xrange(0,rows):
			pict.append(list(raw_input()))
		for i in xrange(0,rows-1):
			for j in xrange(0,cols-1):
				a = pict[i][j]
				b = pict[i][j+1]
				c = pict[i+1][j]
				d = pict[i+1][j+1]
				if a == '#' and b == '#' and c == '#' and d == '#':
					pict[i][j] = "/"
					pict[i][j+1] = "\\"
					pict[i+1][j] = "\\"
					pict[i+1][j+1] = "/"
	
		bluePresent = False
		for i in xrange(0,rows):
			for j in xrange(0,cols):
	 			if pict[i][j] == '#':
					bluePresent = True
					break
	
		print "Case #" + str(case) + ":"
		if bluePresent == True:
			print "Impossible"
		else:
			for row in pict:
				print "".join(row)	

solve()
