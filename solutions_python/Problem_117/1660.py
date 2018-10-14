# lawnmower

file = open('B-small-attempt0.in.txt', 'r')
T = file.readline()
T = int(T)
count = 0
case_number = 1

output = open('Lawnmower_output.txt', 'w')

while (count < T):
	row_column = []
	lawn = []
	status = ''
	
	# read lawn size
	row_column = file.readline().rstrip().split()
	rows = row_column[0]
	rows = int(rows)
	columns = row_column[1]
	columns = int(columns)
	
	#print '\nrows x columns = ', rows, 'x', columns
	
	# read in the lawn heights
	for x in range(0, rows):
		lawn.append(file.readline().rstrip().split())
	
	# test rows, if the 1's span across the whole grid then validate them
	#print 'row validation'
	for line in lawn:
		row_check = 0
		for square in line:
			#print 'square is', square
			if (square == '1'):
				row_check += 1
				#print 'row_check is', row_check
		if (row_check == columns):
			# validate
			#print 'validated row\n'
			for x in range(0, columns):
				line[x] = '3'
		#else:
			#print 'unvalidated row\n'
				

	
	# test columns, if the 1's span across the whole grid then validate them
	#print 'column validation'
	for x in range(0, columns):
		column_check = 0
		for line in lawn:
			#print 'line[x] is', line[x]
			if (line[x] == '1' or line[x] == '3'):
				column_check += 1
				#print 'column check is', column_check
		if (column_check == rows):
			#print 'validated column\n'
			for line in lawn:
				if (line[x] == '1'):
					line[x] = '3'
		#else:
			#print 'unvalidated column\n'
			
	
	
	# test lawn for non-validated 1's, if there are any then not possible
	for line in lawn:
		for square in line:
			if (square == '1'):
				status = 'NO'
	
	if (status != 'NO'):
		status = 'YES'
	
	print 'Case #' + str(case_number) + ': ' + str(status)
	output.write('Case #' + str(case_number) + ': ' + str(status) + '\n')
	
	
	# show lawn
	#for line in lawn:
		#print line
	
	count += 1
	case_number += 1