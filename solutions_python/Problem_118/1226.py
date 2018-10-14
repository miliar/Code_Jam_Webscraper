#!/usr/bin/python
def to_base_3(n):
	s=[]
	while n:
		s.append(str(n%3))
		n=n/3
	return ''.join(s[::-1])

def solve(minimum, maximum):
	#print "max: " + str(maximum)
	#print "min: " + str(minimum)
	i=1
	num=1
	found = 0
	while (num <= maximum):
		num = int(to_base_3(i))
		i+=1

		small_second_part_str = str(i)[0:len(str(num))-1]
		small_num = int(str(num) + small_second_part_str[::-1])
		small_square = small_num * small_num

		if (small_square > maximum):
			break
		
		if (small_square >= minimum):

			if (str(small_square) == str(small_square)[::-1]):
				#print "#################"
				#print "small"
				#print small_num
				#print small_square
				found+=1

		big_num = int(str(num) + str(num)[::-1])
		big_square = big_num * big_num

		if (big_square > maximum):
			continue

		if (big_square >= minimum):

			if (str(big_square) == str(big_square)[::-1]):
				#print "#################"
				#print "big"
				#print big_num
				#print big_square
				found+=1

	if (minimum <= 9) and (maximum >= 9):
		found += 1
	return found
		
import sys
input_lines = open(sys.argv[1], "rt").readlines()
stripped_input_lines = [line.strip() for line in input_lines]
num_tests = int(input_lines[0])
#print num_tests

i=1
for line in stripped_input_lines[1:]:
	minimum = int(line.split()[0])
	maximum = int(line.split()[1])
	result = solve(minimum, maximum)
	print "Case #"+str(i)+": "+str(result)
	i+=1
