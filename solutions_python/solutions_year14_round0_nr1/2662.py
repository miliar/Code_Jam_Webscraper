TABLE_SIZE = 4

with open('input') as input_file:
	"""The file structure is as follows:
	First line - number of test
	Test:
		line - row
		4 lines - table
		line - row
		4 lines - table"""
	def row_as_set():
		row_id = int(input_file.readline()) # Gets row id in table
		row = None
		for i in range(1, TABLE_SIZE+1):
			# Creates a generator for the numerical value of numbers in the line
			line = (int(number) for number in input_file.readline().split())
			if i == row_id: row = set(line) # Casts the line into a set
		return row
		
	test_count = int(input_file.readline())
	# Test loop, prints to file
	with open('output', 'w') as output_file:
		for case in range(1, test_count+1):
			first_row = row_as_set()
			second_row = row_as_set()
			shared = first_row & second_row
			shared_size = len(shared)
			
			if (shared_size == 0):
				message = 'Volunteer cheated!'
			elif (shared_size == 1):
				message = str(shared.pop())
			else:
				message = 'Bad magician!'
			output_file.write('Case #%d: %s\n'%(case, message))
			
	