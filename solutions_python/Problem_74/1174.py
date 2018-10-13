
infile = "A-large.in"
input = open(infile, "r")
outfile = "robots.txt"
output = open(outfile, "w")


test_cases = input.readline()
test_cases = int(test_cases)


for i in range(1, (test_cases+1)):
	line = input.readline().rstrip("\n").split(' ')	
	num_buttons = line[0]
	num_buttons = int(num_buttons)
	line.pop(0)

	O_list = []
	B_list = []
	for j in range(0, len(line)):
		if line[j] == 'O':
			O_list.append(line[j+1])
		if line[j] == 'B':
			B_list.append(line[j+1])

	time = 0
	O = 1
	B = 1
	do_nothing = 1


	while num_buttons > 0:
		time = time + 1
		if len(O_list) > 0:
			o_next = O_list[0]
			o_next = int(o_next)
		if len(B_list) > 0:
			b_next = B_list[0]
			b_next = int(b_next)

		if O == o_next and line[0] == 'O':
			O_list.pop(0)
			line.pop(0)
			line.pop(0)
			num_buttons = num_buttons - 1

		elif B == b_next and line[0] == 'B':
			B_list.pop(0)
			line.pop(0)
			line.pop(0)
			num_buttons = num_buttons - 1

		if O < o_next:
			O = O + 1
		if O > o_next:
			O = O - 1		
		if B < b_next:
			B = B + 1
		if B > b_next:
			B = B - 1



	number = i
	number = str(number)
	output.write("Case #"+number+": ",)
	time = str(time)
	output.write(time)
	output.write('\n')


input.close()
output.close()
