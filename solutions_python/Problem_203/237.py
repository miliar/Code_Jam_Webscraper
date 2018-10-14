import sys

def solve(in_file, out_file, case):
	out_file.write('Case #' + str(case + 1) + ':\n')
	
	line = in_file.readline().replace('\n', '')
	rows = int(line.split(' ')[0])
	cols = int(line.split(' ')[1])
	
	columns = []
	row_index = 0
	while(row_index < rows):
		column = in_file.readline().replace('\n', '')
		columns.append(column)
		row_index += 1
	
	# Duplicate letters up/down/left/right
	last = '?'
	row_index = 0
	while(row_index < rows):
		col_index = 0
		last = '?'
		while(col_index < cols):
			new = columns[row_index][col_index]
			if(new != '?'):
				if(last != new):
					last = new
			else:
				if(last != '?'):
					columns[row_index] = columns[row_index][0:col_index] + last + columns[row_index][(col_index + 1):len(columns[row_index])]
			col_index += 1
		row_index += 1
	
	last = '?'
	row_index = 0
	while(row_index < rows):
		col_index = cols - 1
		last = '?'
		while(col_index >= 0):
			new = columns[row_index][col_index]
			if(new != '?'):
				if(last != new):
					last = new
			else:
				if(last != '?'):
					columns[row_index] = columns[row_index][0:col_index] + last + columns[row_index][(col_index + 1):len(columns[row_index])]
			col_index -= 1
		row_index += 1
	
	last = '?'
	col_index = 0
	while(col_index < cols):
		row_index = 0
		last = '?'
		while(row_index < rows):
			new = columns[row_index][col_index]
			if(new != '?'):
				if(last != new):
					last = new
			else:
				if(last != '?'):
					columns[row_index] = columns[row_index][0:col_index] + last + columns[row_index][(col_index + 1):len(columns[row_index])]
			row_index += 1
		col_index += 1
	
	last = '?'
	col_index = 0
	while(col_index < cols):
		row_index = rows - 1
		last = '?'
		while(row_index >= 0):
			new = columns[row_index][col_index]
			if(new != '?'):
				if(last != new):
					last = new
			else:
				if(last != '?'):
					columns[row_index] = columns[row_index][0:col_index] + last + columns[row_index][(col_index + 1):len(columns[row_index])]
			row_index -= 1
		col_index += 1
	
	row_index = 0
	while(row_index < rows):
		out_file.write(columns[row_index] + '\n')
		row_index += 1

if len(sys.argv) != 2:
	print 'Please provide one parameter with the name of the input file location relative to this file.'
else:
	in_file = open(str(sys.argv[1]), 'r')
	out_file = open(str(sys.argv[1]).replace('.in', '.out'), 'w')
	cases = int(in_file.readline())
	case = 0
	while (case < cases):
		solve(in_file, out_file, case)
		case += 1
	in_file.close()
	out_file.close()