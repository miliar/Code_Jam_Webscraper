# test_cases = ['4', '132', '1000', '7', '111111111111111110']

def is_tidy(n):
	return list(str(n)) == sorted(list(str(n)))

def largest_smaller_tidy(n):
	test_val = n
	while not is_tidy(test_val):
		test_val -= 1

	return test_val

def main():
	for test_num in range(1, int(raw_input()) + 1):
		result = largest_smaller_tidy(int(raw_input()))

		print 'Case #{0}: {1}'.format(test_num, result)

if __name__ == '__main__':
	main()
