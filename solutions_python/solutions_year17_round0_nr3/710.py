from iopart import read_input, write_output

raw_data = read_input(name_of_file = 'C-large.in')

number_of_rows, data = raw_data
final_data = (element.split(' ') for element in data)
final_answer = []

def find_bath(number_of_stalls = 1000, number_of_visitors = 1000, ):
	if number_of_visitors == 1:
		#code
		if number_of_stalls == 1:
			return (0,0)
		return (number_of_stalls//2, (number_of_stalls-1)//2)
	if number_of_stalls % 2 == 0:
		if number_of_visitors % 2 == 0:
			#rigth side
			#half number of stalls
			return find_bath(number_of_stalls//2, number_of_visitors//2)
		else:
			#left side
			#half-1 number of stalls
			return find_bath(number_of_stalls//2 - 1, (number_of_visitors-1)//2 )
	else:
		if number_of_visitors % 2 == 0:
			return find_bath((number_of_stalls-1)//2, number_of_visitors//2)
		else:
			return find_bath((number_of_stalls-1)//2, (number_of_visitors-1)//2)
		 

for element in final_data:
	print(element[1], element[0], type(element[0]))
	a, b = find_bath(number_of_stalls = int(element[0]),
    							  number_of_visitors = int(element[1]))
	final_answer.append(str(a)+' '+str(b))

write_output(final_answer, name_of_file = 'C-large.out')