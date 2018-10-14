import math

def is_palindrome(number):
	number_list = list(str(number))
	number_of_digits = len(number_list)
	for digit_idx in range(0, int(math.ceil(number_of_digits/2))):
		if number_list[digit_idx] != number_list[number_of_digits - digit_idx - 1]:
			return False;
	return True;

def get_list_of_palindromes_in_range(range_tuple):
	palindromes = []
	for i in  range(range_tuple[0], range_tuple[1] + 1):
		if(is_palindrome(i)):
			palindromes.append(i)
	return palindromes

def write_result_to_file(file, case_num,  result):
	file.write("Case #" + str(case_num) + ": " + str(result) + "\n")

f = open('C-small-attempt0.in', 'r')
output = open('output.txt', 'w')
tc_count = f.readline()
#print tc_count
for tc_idx in range(0, int(tc_count)):
	range_str = f.readline()
	range_list = [int(string) for string in range_str.strip().split()]
	sqrt_range_tuple = (int(math.ceil(math.sqrt(range_list[0]))), int(math.floor(math.sqrt(range_list[1]))))
	palindromes = get_list_of_palindromes_in_range(sqrt_range_tuple)
	#print palindromes
	fair_and_square_count = 0
	for palindrome in palindromes:
		if is_palindrome(palindrome*palindrome):
			fair_and_square_count = fair_and_square_count + 1
	write_result_to_file(output, tc_idx + 1,  fair_and_square_count)
