
def last_tidy_number(n):
	''' Returns the last tidy number before n.
	'''
	# print('Input', n)

	if is_tidy(n):
		return n

	number = str(n)

	# If the number is a single digit, it must be tidy.
	if len(number) == 1:
		return n


	for idx, i in enumerate(range(len(number)-1, 0, -1)):
		right_digit = number[i]
		left_digit = number[i-1]
		# print('i', i)
		# print('Left', left_digit) 
		# print('Right', right_digit)

		if int(right_digit) < int(left_digit):

			# print('Untidy number found~!')
			right_digit = '9'
			left_digit = str(int(left_digit) - 1)
			# print('New left digit:', left_digit)
			# print('New right digit:', right_digit)

			# Remember to update the number
			updated_number = number[:i-1] + left_digit + '9'*(idx+1)
			# print('Updated number:', updated_number)

			return last_tidy_number(int(updated_number))



def is_tidy(num):
	''' Returns True if num is Tidy and False otherwise.
	'''

	number = str(num)
	previous_digit = number[0]
	for digit in number:
		if digit < previous_digit:
			return False

		previous_digit = digit
	return True

if __name__ == '__main__':

	num_test_cases = int(input())

	for i in range(num_test_cases):

		n = int(input())

		result_string = last_tidy_number(n)

		print('Case #{}: {}'.format(i+1, result_string))

