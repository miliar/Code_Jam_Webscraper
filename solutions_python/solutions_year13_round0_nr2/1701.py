class testcase_class():
	rows = None
	columns = None
	data = None

	smallest = 1000
	smallest_position = (-1, -1)

	def find_smallest(self):

		self.smallest = 1000
		self.smallest_position = (-1, -1)

		for y in range(self.rows):
			for x in range(self.columns):
				if self.data[y][x] != '*' and int(self.data[y][x]) < self.smallest:
					self.smallest = int(self.data[y][x])
					self.smallest_position = (x, y)

		return self.smallest, self.smallest_position

	def check_row(self):

		row = self.data[self.smallest_position[1]]
		
		for element in row:
			if element != '*' and int(element) != self.smallest:
				return False

		self.data[self.smallest_position[1]] = ['*']*self.columns

		return True

	def check_column(self):

		column = []

		for row in self.data:
			column += row[self.smallest_position[0]]

		
		
		for element in column:
			if element != '*' and int(element) != self.smallest:
				return False

		for row in self.data:
			row[self.smallest_position[0]] = '*'

		return True


input_file = open('in2.txt', 'r+')
input_data = input_file.read()
input_file.close()

input_data = input_data.split('\n')

testcases_number = int(input_data[0])

input_data.pop(0)


for i in range(len(input_data)):
	input_data[i] = input_data[i].split()

output = ''

for t in range(testcases_number):

	testcase = testcase_class()
	testcase.rows = int(input_data[0][0])
	testcase.columns = int(input_data[0][1])
	testcase.data = input_data[1:testcase.rows + 1]
	input_data = input_data[testcase.rows + 1:]

	while testcase.find_smallest() != (1000, (-1, -1)):
		if not testcase.check_row() and not testcase.check_column():
			output += "Case #%i: NO\n" % (t+1)
			break

		if testcase.find_smallest() == (1000, (-1, -1)):
			output += "Case #%i: YES\n" % (t+1)
		#print "OK", testcase.data, testcase.find_smallest() != (1000, (-1, -1))
	# while there is smallest (i.e. not just *):
		# if not check_row and not check_column:
			# not possible

	# possible

	#NOTE: check_row should change to * and return True if posisble

#print input_data

output_file = open('out2.txt', 'r+')
output_file.write(output)
output_file.close()