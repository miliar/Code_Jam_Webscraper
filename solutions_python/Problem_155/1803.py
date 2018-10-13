import fileinput

line_num = 0
answers = []

for line in fileinput.input():
	
	# Don't need number of test cases for this solution; ignore first line.
	if line_num == 0:
		pass
	else:
		lines = line.split(' ')
		shyness_array = lines[1]
		standers = 0
		j = 0
		num_friends = 0

		while j < len(shyness_array) - 1 and standers < len(shyness_array):

			print j
			print shyness_array[j]
			if(int(shyness_array[j])) > 0:
				standers += int(shyness_array[j])
				standers -= 1
			else:
				if standers > 0:
					standers -= 1
				else:
					num_friends += 1
			j += 1

		answers.append(num_friends)

	line_num += 1

f = open('answer.txt', 'w')
for case, solution in enumerate(answers):
	f.write("Case #{}: {}\n".format(case+1, solution))
f.close()












