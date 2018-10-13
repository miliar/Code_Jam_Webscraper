import numpy
import operator

input = open('input.in', 'r')
output = open('output.txt', 'a')


num_inputs = input.readline().strip()

def separate(number):
	group = list(map(int,str(number)))
	group_1 = numpy.roll(group,-1).tolist()
	
	if sorted(group) == group:
		return number
	else:

		group_2 = group_1[:-1] + [0]
			
		group_3 = list(map(operator.sub, group_2, group))
		group_4 = list(group_3)
		
		# print(list(map(operator.sub, group_1, group_2))
		val = next((index for index,value in enumerate(group_3) if value <= 0), None)
		
		group[val] = group[val] -1
		updated = group[0:val+1]+[9]*(len(group)-(val+1))
		
		return int("".join(map(str, updated)))


for i in range(int(num_inputs)):
	answer = separate(input.readline().strip())
	output_string = 'Case #' + str(i+1) + ':' + ' ' + str(answer)
	print(output_string)
	output.write(output_string+'\n')


# num_inputs = input.readline().strip()
