def parse_input(str):
    str_first_val = str.split()
    real_digits = [ int(c) for c in str_first_val[0] ]
    return real_digits


def solve(test):
	big_number = parse_input(test)
	
	num_of_digits = len(big_number)
	
	index_of_max_incrising_digit = 0
	for digit_ind in range(0,num_of_digits):
		if( big_number[digit_ind] > big_number[index_of_max_incrising_digit] ):
			index_of_max_incrising_digit = digit_ind;
		elif ( big_number[digit_ind] < big_number[index_of_max_incrising_digit] ):
			big_number[index_of_max_incrising_digit] -= 1
			for digit_ind_in_change in range(index_of_max_incrising_digit+1,num_of_digits):
				big_number[digit_ind_in_change] = 9
			break

	num_in_str = ''.join(map(str,big_number))
	
	if( num_in_str[0] == '0'):
		num_in_str = num_in_str[1:]
	return num_in_str