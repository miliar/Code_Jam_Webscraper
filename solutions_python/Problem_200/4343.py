import numpy
import operator

input = open('input.in', 'r')
output = open('output.txt', 'a')


num_inputs = input.readline().strip()
print(num_inputs)

def separate(number):
	group = list(map(int,str(number)))
	group_1 = numpy.roll(group,-1).tolist()
	
	if sorted(group) == group:
		return number
	else:

		group_2 = group_1[:-1] + [0]
			
		group_3 = list(map(operator.sub, group_2, group))
		group_4 = list(group_3)
		
		#ie 5622
		val = next((index for index,value in enumerate(group_3) if value < 0), None)

		#special cases
		#ie 111111111110
		if val>0 and sum(group_3[0:val]) == 0:
			val = next((index for index,value in enumerate(group_3) if value <= 0), None)
		
		#ie 11223344406
		#find the first negative, by leading 0, but not from the beginning
		#correctly capture where 0 nearest first negative happens
		elif val >0 and 0 in group_3[0:val]:
			
			#pick up zeros
			group_short = list(group_3[0:val])
		
			group_short_bi = [ x == 0 for x in group_short]
		
			val = len(group_short_bi)  - next((index for index, value in enumerate(reversed(group_short_bi)) if value == False),None)
		

		group[val] = group[val] -1
		updated = group[0:val+1]+[9]*(len(group)-(val+1))
		

		return int("".join(map(str, updated)))


for i in range(int(num_inputs)):
	answer = separate(input.readline().strip())
	output_string = 'Case #' + str(i+1) + ':' + ' ' + str(answer)
	print(output_string)
	output.write(output_string+'\n')


# num_inputs = input.readline().strip()
