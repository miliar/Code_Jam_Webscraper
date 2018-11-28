#!/usr/bin/python
import sys

class point:
	def __init__(self, label, vendors):
		self.label = label
		self.vendors = vendors
		
data = sys.stdin.readlines()
cases = int(data.pop(0))
case = 1

while (case <= cases):
	temp = data.pop(0).split()
	num_rows = int(temp[0])
	rows = []
	num_columns = int(temp[1])
	for row in range(1, num_rows+1):
		rows.append(list(data.pop(0)))
		
	# # =blue  . =white
	failed = False
	row_index = 0
	for row in rows:
		column_index = 0
		for col in rows[row_index]:
			changed = False
			if row[column_index] == '#':
				if column_index < num_columns-1 and row_index < num_rows-1:
					if row[column_index+1] == '#':
						if rows[row_index+1][column_index] == '#':
							if rows[row_index+1][column_index+1] == '#':
								rows[row_index][column_index] = '/'
								rows[row_index][column_index+1] = '\\'
								rows[row_index+1][column_index] = '\\'
								rows[row_index+1][column_index+1] = '/'
								changed = True
				if changed is False:
					failed = True
			column_index += 1
		row_index += 1
		
	sys.stdout.write("Case #%d:\n" % case)
	
	
	if failed is True:
		sys.stdout.write("Impossible\n")
	else:
		for row in rows:
			for col in row:
				sys.stdout.write(col)
	case += 1