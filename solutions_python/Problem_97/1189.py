input_file_lines = open("C-small-attempt0.in").readlines()
del input_file_lines[0]

for line_number, line in enumerate(input_file_lines):
	result = "Case #" + str(line_number + 1) + ": "
	start, end = line.split(" ", 1)
	count = 0
	for n in range(int(start), int(end) + 1):
		digits = list(str(n))
		for m in range(int(start), int(end) + 1):
			if m > n:
				seen = []
				recycled_digits = list(str(m))
				for moves in range(len(recycled_digits)):
					last_digit = recycled_digits[-1]
					for digit_index, digit in reversed(list(enumerate(recycled_digits))):					
						try:
							recycled_digits[digit_index + 1] = recycled_digits[digit_index]
						except IndexError:
							pass
					recycled_digits[0] = last_digit
					if recycled_digits == digits and "".join(recycled_digits) not in seen:
						seen.append("".join(recycled_digits))
						count += 1					
	print result + str(count)
