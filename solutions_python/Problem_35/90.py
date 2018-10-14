import sys

values = []
sinkNum = {}
basin = []

def getBasin(row, col):
	if basin[row][col] != '0':
		return basin[row][col]
		
	n = values[row-1][col]
	w = values[row][col-1]
	e = values[row][col+1]
	s = values[row+1][col]
	
	minimum = min(min(n,s), min(e,w))
	if not minimum < values[row][col]:
		#make this the sink
		basin[row][col] = chr(ord('a') + sinkNum[0])
		sinkNum[0] = sinkNum[0] + 1
	else:
		#n w e s
		if n <= w and n <= e and n <= s:
			basin[row][col] = getBasin(row-1, col)
		elif w <= e and w <= s:
			basin[row][col] = getBasin(row, col-1)
		elif e <= s:
			basin[row][col] = getBasin(row, col+1)
		else:
			basin[row][col] = getBasin(row+1, col)
			
	return basin[row][col]
			
input = sys.stdin

for i in range (0, int(input.readline())):
	(r, c) = input.readline().split(' ')
	(ri, ci) = (int(r), int(c))
	
	#print ri, ci
	
	del basin[:]
	del values[:]
	
	for r1 in range(0, ri+2):
		basin.append(['0'] * (ci+2))
		values.append([70000] * (ci+2))
	
	for row in range(0, ri):
		rr = input.readline().split(' ')
		for col in range(0, ci):
			values[row+1][col+1] = int(rr[col])
			
	sinkNum[0] = 0
	
	#print values
	
	print "Case #%d: " % (i+1,)
	for row in range(0, ri):
		for col in range(0, ci):
			print getBasin(row+1, col+1),
		print ""