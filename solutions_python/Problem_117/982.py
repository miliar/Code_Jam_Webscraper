import numpy as np

def check_square(garden,row,col):
	return (garden[row][col] >= garden[max(row-1,0)][col] \
		and garden[row][col] >= garden[min(row+1,garden.shape[0]-1)][col]) \
		or (garden[row][col] >= garden[row][max(0,col-1)] \
		and garden[row][col] >= garden[row][min(col+1,garden.shape[1]-1)])

def check_feasible(garden):
	max_in_rows = []
	for i in range(garden.shape[0]):
		row_max = 0
		for j in range(garden.shape[1]):
			row_max = max(row_max,garden[i][j])
		max_in_rows.append(row_max)

	max_in_cols = []
	for j in range(garden.shape[1]):
		col_max = 0
		for i in range(garden.shape[0]):
			col_max = max(col_max,garden[i][j])
		max_in_cols.append(col_max)

	for i in range(garden.shape[0]):
		for j in range(garden.shape[1]):
			if garden[i][j] != min(max_in_rows[i],max_in_cols[j]):
				return False
	return True

for i in range(1,int(raw_input())+1):
	dim = raw_input().split()
	garden = np.ndarray(shape=(int(dim[0]),int(dim[1])),dtype=int)
	for row in range(int(dim[0])):
		line = raw_input().split()
		for col in range(int(dim[1])):
			garden[row][col] = line[col]
	print 'Case #%d: %s' % (i,'YES' if check_feasible(garden) else 'NO')