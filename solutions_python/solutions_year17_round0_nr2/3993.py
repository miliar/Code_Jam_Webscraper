
def calculate_tiny_number(input_str):
	input_num = int(input_str)
	input_str = str(input_num)
	prev_dig = 0
	for i in range(0, len(input_str)):
		if int(input_str[i]) >= prev_dig:
			prev_dig = int(input_str[i])
		else:
			input_str = decrement_num(input_str, i)
			break;
	
	return int(input_str)

def decrement_num(input_str, pos):
	#if pos == len(input_str):
	#	input_str = input_str[0:pos].join('9')
	#else:
	#	input_str = input_str[0:pos] + '9' + (input_str[pos+1: len(input_str)])

	# input_str[pos] = '9'
	if check_tidy_num(input_str) == True:
		return input_str
	if pos > 0:
		char_pos_minus = input_str[pos-1]
		if char_pos_minus == '1':
			num_nines = len(input_str) - pos
			n = ''.join(['9' for s in range(num_nines)])
			if pos-1 == 0:
				input_str = " "+n
			else:

				input_str = decrement_num(input_str, pos-1)
		else:
			char_pos_minus = str(int(char_pos_minus)-1)
			num_nines = len(input_str) - pos
			n = ''.join(['9' for s in range(num_nines)])
			if pos-1 == 0:

				input_str = char_pos_minus+ n
			else:
				input_str = decrement_num(input_str[0:(pos-1)]+(char_pos_minus)+n, pos-1)

	return input_str


def check_tidy_num(input_num):
	str_num = str(input_num)
	prev = 0;
	for i in range(0, len(input_num)):
		digit = int(str_num[i])
		if digit < prev:
			return False
		prev = digit

	return True

def main():
	f = open('input.txt', 'r')
	f.readline()
	case = 1
	for line in f:
		if len(line) == 1:
			tidy_num = int(line)
		else:
			tidy_num = calculate_tiny_number(line)

		print("Case #"+str(case)+": "+str(tidy_num))
		case += 1


if __name__ == "__main__": main()
