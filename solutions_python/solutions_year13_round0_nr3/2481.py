from math import sqrt

def palindrome(number):
	return str(number) == str(number)[::-1]

def scan_range(A, B):
	fair_square_numbers = []
	root = int(sqrt(A))
	if root**2 < A:
		root += 1

	while(root**2 <= B):
		if palindrome(root**2) and palindrome(root):
			fair_square_numbers.append(root**2)
		root += 1

	return fair_square_numbers

def read_file(filename):
    f = open(filename, 'r')
    results = []
    cases = int(f.readline())

    for case in range(1, cases + 1):
        parts = f.readline().split()
        A = int(parts[0])
        B = int(parts[1])

        result = 'Case #{0}: {1}'.format(case, len(scan_range(A, B)))
        results.append(result)
        print(result)

    return results

def write_file(filename, results):
    f = open(filename, 'w')

    for line in results:
        f.write(line + '\n')

if __name__ == '__main__':
    filename = raw_input('Input Filename: ')
    results = read_file(filename)

    filename = raw_input('Output Filename: ')
    write_file(filename, results)
