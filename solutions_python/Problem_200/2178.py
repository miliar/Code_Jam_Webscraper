total_nums = int(input())

results = [0 for i in range(total_nums)]

for j in range(total_nums):

	str_num = input()

	digits = [int(x) for x in str_num]

	for i in range(len(digits) - 2, -1, -1):
		if digits[i] > digits[i + 1]:
			digits[i] -= 1
			digits[i + 1:] = [9] * (len(digits) - i - 1)

	str_result = ''
	for digit in digits:
		str_result += str(digit)

	results[j] = int(str_result)

for i in range(total_nums):
	print('Case #{}: {}'.format(i + 1, results[i]))
