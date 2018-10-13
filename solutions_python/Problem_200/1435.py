def lastTidy(n):
	digits = list(str(n))

	i = 1
	while i < len(digits):
		if int(digits[i]) < int(digits[i - 1]):
			j = i - 1
			while j > 0:
				if int(digits[j - 1]) == int(digits[j]):
					j -= 1
				else:
					break
			digits[j] = str(int(digits[j]) - 1)
			digits[j + 1:] = ['9'] * (len(digits) - (j + 1))
			break
		i += 1

	if digits[0] == '0':
		return ''.join(digits[1:])
	return ''.join(digits)

n = int(input())
for i in range(n):
	number = int(input())
	print('Case #{}: {}'.format(i + 1, lastTidy(number)))

