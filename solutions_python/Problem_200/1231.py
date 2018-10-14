t = int(raw_input())
answers = []
for i in range(0, t):
	digits = []
	in_str = raw_input()
	for digit in in_str:
		digits.append(int(digit))

	for i in range(0, len(digits) - 1):
		if digits[-(i+1)] < digits[-(i+1)-1]:
			digits[-(i+1)-1] -= 1
			for j in range(0, i+1):
				digits[-(j+1)] = 9

	while digits[0] == 0:
		digits.pop(0)
	answers.append(digits)

for i in range(0, t):
	out_str = "Case #" + str(i+1) + ": "
	for digit in answers[i]:
		out_str += str(digit)
	print out_str
