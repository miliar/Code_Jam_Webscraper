import csv

count = 1
length = 0
data = []

with open('problem_1_input.txt', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter= ' ')
	for row in reader:
	    if count == 1:
	    	length = row[0]
	    else:
	    	data.append(row)
	    count += 1

def flip(array, start_index, num_flip):
	#print "array: ", array, " start_index ", start_index, " num_flip ", num_flip
	for i in range(num_flip):
		if array[start_index + i] == '-':
			array[start_index + i] = '+'
		else:
			array[start_index + i] = '-'

def check(array):
	for i in array:
		if i == '-':
			return 0
	return 1

case_num = 0
status = ''
for row in data:
	case_num += 1
	string = row[0]
	num_flip = row[1]
	array = list(string)
	count = 0
	for i in range(len(array) - int(num_flip) + 1): 
		if array[i] == '-':
			flip(array, i, int(num_flip))
			count += 1
	if check(array) == 1:
		status += 'Case #' + str(case_num) + ': ' + str(count) + '\n'
	else:
		status += 'Case #' + str(case_num) + ': IMPOSSIBLE' + '\n'
			
print status
with open('problem_1_output.txt', 'w') as out:
	out.write(status)
			
