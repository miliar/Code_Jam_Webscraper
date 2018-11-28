import math

input_file = open("C-small-attempt0.in", 'r')
output_file = open("squareoutput.txt",'w')
no_of_cases = input_file.readline().strip()
for i in range(1,int(no_of_cases)+1):
	count = 0
	intervel = input_file.readline().strip()
	intervel_start , intervel_end = intervel.split(' ')
	interval_check_squares_end = math.sqrt(int(intervel_end))
	interval_check_squares_start = math.ceil(math.sqrt(int(intervel_start)))
	for x in range(int(interval_check_squares_start),int(interval_check_squares_end)+1):
		number = str(x)
		square = str(x*x)
		if (number == number[::-1]) and (square == square[::-1]):
			count = count+1
	output_file.write("Case #{0}: {1} \n".format(i,count))