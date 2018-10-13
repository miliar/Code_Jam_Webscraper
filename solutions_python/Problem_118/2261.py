from math import sqrt

def result(case_index, a, b):
	return 'Case #{0}: {1}\n'.format(
			case_index + 1, fairs_and_squares(a, b))

def fairs_and_squares(a, b):
	count = 0
	for i in range(int(a), int(b) + 1):
		if is_palindrome(i) and is_palindrome(sqrt(i)):
			count += 1
	return count

def is_palindrome(number):
	number = str(number)
	if number[-2:] == '.0':
		number = number[:-2]
	return number == number[::-1]

def main():
	lines = filter(None, open('C-small-attempt0.in').read().splitlines())
	number_of_test_cases, lines = int(lines[0]), lines[1:]
	
	output = open('output', 'w')

	for i in range(number_of_test_cases):
		a, b = lines.pop(0).split()
		output.write(result(i, a, b))
	output.close()



if __name__ == "__main__":
	    main()
