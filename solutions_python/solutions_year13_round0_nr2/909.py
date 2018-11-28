from pprint import pprint as pp

ncases = int(raw_input().strip())

for case_i in range(ncases):
	n, m = map( int, raw_input().strip().split(' ') )
	matrix = []
	matrix_t = []
	matrix_r_max = []
	for n_i in range(n):
		try:
			line = map( int, raw_input().strip().split(' ') )
		except:
			break

		matrix.append( line )
		matrix_r_max.append( max(line) )

	matrix_c_max = [ max(each) for each in zip(*matrix) ]

	r = (min([
	 	matrix_r_max[row] == matrix[row][col] or
	 	matrix_c_max[col] == matrix[row][col]
	 	for row in range(len(matrix))
	 		for col in range(len(matrix[row])) 
		]))

	print "Case #%d: %s" % ( case_i+1, [ 'NO', 'YES' ][ r == True ] )

	# pp (matrix_r_max)
	# pp (matrix_c_max)
