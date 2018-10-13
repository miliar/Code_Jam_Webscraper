import fileinput
from decimal import *

input_array = []
for line in fileinput.input():
	input_array.append(line)

# input_array = input_string.rstrip().split("\n")
test_cases = int(input_array[0])

f = open('q2_output.txt', 'w')
for x in xrange(0, test_cases):
	test_array = map(Decimal, input_array[x+1].rstrip().split(" "))
	val_c = test_array[0]
	val_f = test_array[1]
	val_x = test_array[2]


	cookies_per_sec = 2
	total_time = 0
	while True:
		time_to_x = val_x/cookies_per_sec
		time_to_f = val_c/cookies_per_sec
		time_to_x_with_f = (val_x)/(cookies_per_sec+val_f)+time_to_f

		if time_to_x_with_f < time_to_x:
			cookies_per_sec += val_f
			total_time += time_to_f
		else:
			f.write("Case #" + str(x+1) + ": " + str(total_time + time_to_x) + "\n")
			break
