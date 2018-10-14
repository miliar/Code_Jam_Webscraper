import sys

input_list = []
output_list = []

def codejam(case_input):
	for x in range(len(case_input)):
		for y in range(len(case_input[x])):
			if check_case(case_input, x, y) == False:
				return 'NO'
	return 'YES'

def check_case(case_input, row, col):
#	print 'check', case_input, row, col
	is_possible_row = True
	is_possible_col = True

	# in a row
	for a in case_input[row]:
		if a > case_input[row][col]:
			is_possible_row = False
			break
	
	for x in range(len(case_input)):
		a = case_input[x][col]
		if a > case_input[row][col]:
			is_possible_col = False
			break
	
	return is_possible_row or is_possible_col

try:
	input_filename = sys.argv[1]
	output_filename = input_filename[:sys.argv[1].find('.')]+'.out'
except:
	print 'input filename as argv'
	exit()

try:
	input_f = open("./"+input_filename)
	input_lines = input_f.readlines()
	input_count = 0
	row_count = 0
	input_case = []
	input_lines.pop(0)
	for input_line in input_lines:
#		print input_line
		input_split = input_line.split()
		if row_count == 0:
			row_count = int(input_split[0])
			continue
		else:
			input_case.append(input_split)
			input_count += 1
#			print row_count , input_count, 'done'
		
		if input_count == row_count:
#			print 'new'
			input_list.append(input_case)
			input_case = []
			input_count = 0
			row_count = 0
		else:
#			print 'old', input_count, row_count
			pass

	input_f.close()
except:
	print 'read error'
	exit()

#print input_list
#input_list.pop(0)

for input_line in input_list:

	# do some works here
	result = codejam(input_line)
	output_list.append([result])

try:
	output_f = open("./"+output_filename, "w")
	output_f.close()
except:
	pass

try:
	output_f = open("./"+output_filename, "a")
	output_str = ''

	for x in range(len(output_list)):
		output_f.write('Case #' + str(x+1)+': '+str(output_list[x][0])+"\n")
		print x
	output_f.close()
except:
	print 'write error'
	exit()
