import sys

outfile = open("output.txt","w")


def geti():							# get some integer
	return int(sys.stdin.readline())

def getis():						# get integer array
	return [int(i) for i in sys.stdin.readline().split()]
	
def pcase(case, output, fl = 0):	# print case
	ans = "Case #" + str(case) + ": " + str(output) + "\n"
	print(ans,end="")
	if fl:
		fl.write(ans)
	

# cut maybe?
def checkrow(grid, row, m, num):
	c = num
	for x in range(m):
		if c != grid[row][x]:
			return 0
	return 1
def checkcol(grid, col, n, num):
	c = num
	for y in range(n):
		if c != grid[y][col]:
			return 0
	return 1
	
	
	
# largest from grid
def getlargest(grid,max):
	h = -1
	for y in grid:
		for x in y:
			if x > h:
				if x >= max:	continue
				else:	h = x
	return h

# smallest from grid
def getsmallest(grid):
	h = 100
	for y in grid:
		for x in y:
			if x < h:
				h = x
	return h

# check if matrixes are equal
def compmatrix(ma, mb, n, m):
	for y in range(n):
		for x in range(m):
			if ma[y][x] != mb[y][x]:
				return 0
	return 1
	
cases = geti()
print("Cases: " + str(cases))

for case in range(1, cases + 1):
	n,m = getis()

	grida = [[0 for i in range(m)] for i in range(n)]
	
	
	for y in range(n):
		grida[y] = [int(i) for i in sys.stdin.readline().split()]

	# cut largest size
	h = getlargest(grida, 100)
	#print("largest: " + str(h))
	gridb = [[h for i in range(m)] for i in range(n)]
	
	s = getsmallest(grida)
	#print("smallest: " + str(s))
	
	while h > s:
		h = getlargest(grida, h)
		#print("largest: " + str(h))
		for y in range(n):
			for x in range(m):
				if grida[y][x] == h:
					# als niet col en niet row, deud
					if checkrow(grida, y, m, h) == 1:
						gridb[y] = [h for i in range(m)]
					if checkcol(grida, x, n, h) == 1:
						for e in range(n):
							gridb[e][x] = h				


	if compmatrix(grida, gridb, n, m) == 1:	pcase(case, "YES", outfile)
	else:	pcase(case, "NO", outfile)
	