import itertools

def vector_sum(v1,v2):

	result = []

	for i in range(0,len(v1)):
		result.append(v1[i]+v2[i])

	return result

file = open('A-large.in', 'r')

input = file.readlines()

number_of_lines = int(input[0])

answer = []
case_number = 1

f = open('output.out','w')

counter = 2
tag = 0
number_of_flavors = 0
flavors = []
batches = []

for i in range (1,len(input)):
	
	req = 0
	present = 0

	input_array = input[i].split(' ')

	number = input_array[1][:-1]
	number_array = []

	for c in number:
		number_array.append(int(c))

	for j in range (0,len(number_array)):

		present += number_array[j]

		while present <= j:
			req += 1
			present += 1

	output_line = 'Case #' + str(i) + ': ' + str(req)
	f.write(output_line + '\n') 
	#print req

f.close()

