import numpy as np

T = int(raw_input())

def not_solvable(n_row, n_col):
	#if n_row == 1 or n_col == 1:
		#return False
	A = []
	for i_row in xrange(n_row):
		A.append([int(i) for i in raw_input().split()])
	A = np.array(A)
	row_max = [-1]*n_row
	col_max = [-1]*n_col
	for i_row in xrange(n_row):
		row_max[i_row] = max(A[i_row,:])
	for i_col in xrange(n_col):
		col_max[i_col] = max(A[:,i_col])
	#print A
	#print row_max
	#print col_max
	return any((A[i_row][i_col]<row_max[i_row] and A[i_row][i_col]<col_max[i_col]) for i_row in xrange(n_row) for i_col in xrange(n_col))
	
for t in xrange(T):
	n_row, n_col = [int(i) for i in raw_input().split()]
	print "Case #%d: %s" % (t+1, "NO" if not_solvable(n_row, n_col) else "YES")
