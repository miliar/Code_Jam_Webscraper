import gmpy2
import math
MAX_VALUE = 10**7+1
def is_palindrome(test_number):
	string_number = str(test_number)
	num_length = len(string_number)
	for index in range(int(math.ceil(num_length/2))):
		if string_number[index] != string_number[len(string_number) - 1 - index]:
			return False
	return True

square_palindrome_list = []
palindrome_dict = {}
test_num = 1
while test_num <= MAX_VALUE:
	if is_palindrome(test_num):
		palindrome_dict[test_num] = True
		square_of_test_num = test_num**2
		if is_palindrome(square_of_test_num):
			square_palindrome_list.append(square_of_test_num)
	test_num +=1

input_file = open('C-large-1.in', 'r')
output_file = open('C-large-1.out', 'w+')
line = input_file.readline()
num_cases = int(line)
for case_num in range(1,num_cases+1):
	result = 0
	low_and_high = input_file.readline().split()
	low_value = int(low_and_high[0])
	high_value = int(low_and_high[1])

	for square_palindrome in square_palindrome_list:
		if low_value <= square_palindrome and high_value >= square_palindrome:
			result +=1

	output_file.write('Case #'+str(case_num)+': '+str(result)+'\n')