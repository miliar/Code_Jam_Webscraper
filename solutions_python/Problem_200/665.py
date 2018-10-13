import sys


if len(sys.argv) < 2:
	print "provide input file"
	exit ()


def load_problem():
	input_file = open(sys.argv[1])
	cases = []
	n = int(input_file.readline())
	for i in range (0, n):
		num = int(input_file.readline())
		cases += [num]
	input_file.close()
	return cases


def split_into_digits(number):
	digits = []
	for s in str(number):
		digits += [int(s)]
	return digits

def digits_to_num(digits):
	num = ""
	for digit in digits:
		num += str(digit)
	return int(num)


def find_error(digits):
	if len(digits) > 1:
		for i in range(0, len(digits)-1):
			if digits[i] > digits[i+1]:
				return i
	return -1


def prettify(num):
	digits = split_into_digits(num)

	error_index = find_error(digits)
	if error_index == -1:
		return digits_to_num(digits)
	else:
		power_of_ten = len(digits) - error_index - 1
		for j in range(error_index + 1, len(digits)):
			digits[j] = 9
		return prettify(digits_to_num(digits) - 10**power_of_ten)


def compute_output():
	cases = load_problem()
	output = open(sys.argv[1] + ".out", "w")
	for i in range(0, len(cases)):
		output.write("Case #{}: {}\n".format(i + 1, prettify(cases[i])))
	output.flush()
	output.close()


if __name__ == "__main__":
	compute_output()
