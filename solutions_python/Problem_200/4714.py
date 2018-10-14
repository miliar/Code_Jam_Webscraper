
def digits(x):
	return 

def tidy_numbers(x):
	if x < 10:
		return x

	end_digits = [0]
	digits = [int(i) for i in str(x)]

	for i in range(len(digits)):
		n = digits[i]

		if i == len(digits)-1 or n <= digits[i+1]:
			end_digits.append(n)
			continue
		
		if n > end_digits[-1]:
			end_digits.append(n-1)
			end_digits.extend([9] * (len(digits)-i-1))
			break

		while n == end_digits[-1]:
			i -= 1
			end_digits.pop()


		end_digits.append(end_digits[-1] or digits[0]-1)
		end_digits.extend([9] * (len(digits)-i-1))

		break


	return int(''.join([str(i) for i in end_digits]))

numbers =   []
should_be = [129,  999, 7,  9999, 899, 789, 459, 449, 399, 4599, 899999, 8999, 11222999]

# for i, x in enumerate(numbers):
# 	print("Case #%s: %s - %s" % (i+1, tidy_numbers(x), should_be[i]))


q = -1
with open("input-b") as f:
	for line in f:
		q += 1
		if q == 0:
			continue
		print("Case #%s: %s" % (q, tidy_numbers(int(line))))
		