## 
def serve(grid):
	nRow = len(grid)
	nCol = len(grid[0])
	nonempty = [] # Initialize list of non-empty rows
	for i in range(nRow):
		flag = 1 # Indicates that no initials were encountered until jth entry
		for j in range(nCol):
			if grid[i][j] == '?':
				if flag == 0:
					grid[i][j] = grid[i][j-1]
			else:
				if i not in nonempty:
					nonempty.append(i)
				if flag == 1:
					grid[i][0:j] = [grid[i][j]]*j
					flag = 0 


	## Fill empty rows
	for i in range(nRow):
		if i < nonempty[0]:
			grid[i] = grid[nonempty[0]]
		elif i not in nonempty:
			grid[i] = grid[i-1]

	return grid



#grid = [['?','?'],['A','?'],['?','B'],['?','?']]
#print serve(grid)
#print serve([['G','?','?'],['?','C','?'],['?','?','J']])
#print serve([['C','O','D','E'],['?','?','?','?'],['?','J','A','M']])
#print serve([['C','A'],['K','E']])


## I/O Handler
fIn = open('A_1.txt', 'r')
fOut = open('A_1_sol.txt','w+')
nCases = int(fIn.readline())
for i in range(nCases):
	t = fIn.readline()
 	nRow, nCol = t.split(" ")
 	nRow = int(nRow)
 	nCol = int(nCol)
 	grid = [[None for j in range(nCol)] for k in range(nRow)] # Initialize grid
 	for j in range(nRow):
 		t = fIn.readline()
 		for k in range(nCol):
 			grid[j][k] = t[k]  
 	ans = serve(grid)
 	output = "Case #{}:\n".format(i+1)
 	fOut.write(output)
 	for j in range(nRow):
 		output = ''.join(ans[j]) + "\n"
 		fOut.write(output)
fIn.close
fOut.close


