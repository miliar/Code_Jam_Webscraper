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
	
def checkhor(grid):
	# check horizontaal
	for y in range(4):
		c = grid[y][0]
		if c == '.':
			continue
		cnt = 0
		#print(c)
		for x in range(4):
			if grid[y][x] == c or grid[y][x] == 'T':
				cnt += 1
				if cnt == 4:
					return c
			else:
				break
	return 0
	
def checkvert(grid):
	# check horizontaal
	for x in range(4):
		c = grid[0][x]
		if c == '.':
			continue
		cnt = 0
		#print(c)
		for y in range(4):
			if grid[y][x] == c or grid[y][x] == 'T':
				cnt += 1
				if cnt == 4:
					return c
			else:
				break
	return 0
	
# diagonaal links
def checkdiagl(grid):
	a = grid[0][0]
	if a == '.':
		return 0
	if grid[1][1] == a or grid[2][2] == 'T':
		if grid[2][2] == a or grid[2][2] == 'T':
			if grid[3][3] == a or grid[3][3] == 'T':
				return a
	return 0
# diagonaal rechts
def checkdiagr(grid):
	a = grid[0][3]
	if a == '.':
		return 0
	if grid[1][2] == a or grid[1][2] == 'T':
		if grid[2][1] == a or grid[2][1] == 'T':
			if grid[3][0] == a or grid[3][0] == 'T':
				return a
	return 0
				
cases = geti()
print("Cases: " + str(cases))

for case in range(1, cases + 1):
	
	grid = [''] * 5
	
	for y in range(4):
		grid[y] = sys.stdin.readline().strip('\n')
	sys.stdin.readline()
	
	
	r = checkhor(grid)
	if r != 0:
		pcase(case, r + " won", outfile)
		continue
	r = checkvert(grid)
	if r != 0:
		pcase(case, r + " won", outfile)
		continue
		
	r = checkdiagl(grid)
	if r != 0:
		pcase(case, r + " won", outfile)
		continue
		
	r = checkdiagr(grid)
	if r != 0:
		pcase(case, r + " won", outfile)
		continue
				
	flag=0
	for x in grid:
		if '.' in x:
			pcase(case, "Game has not completed", outfile)
			flag=1
			break
	if flag==0:
		pcase(case, "Draw", outfile)

	