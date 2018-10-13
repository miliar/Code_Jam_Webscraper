cases = int(input())

for case_num in range(1,cases+1):
	number_string = input()
	length = len(number_string)
	digits = list(map(int, list(number_string)))
	
	increasing = True
	pos = 0
	for i in range(1,length):
		if digits[i] < digits[i-1]:
			increasing = False
			pos = i
			break
	
	if increasing:
		print("Case #%d: " % (case_num) + number_string)
		continue

	pos -= 1

	# Here the ith digit is less than the i-1th digit.
	while pos > 0:
		if digits[pos] == digits[pos - 1]:
			pos -= 1
		else:
			break
	
	digits[pos] -= 1
	while pos < length - 1:
		digits[pos + 1] = 9
		pos += 1

	print("Case #%d: " % (case_num) + str(int("".join(map(str,digits)))))
