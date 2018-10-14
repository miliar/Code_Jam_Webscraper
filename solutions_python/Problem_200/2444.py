def findIntAtPlace(integer, length):
	intsAtPlace = []
	i = 0
	while length > 0:
		intsAtPlace.append(integer // (10 ** (length - 1)) % 10)
		i += 1
		length -= 1
	return intsAtPlace

def findTidyNumber(values):
	i = 0
	while i < len(values) - 1:
		if (values[i] > values[i + 1]):
			values[i] -= 1
			for j in range(i + 1, len(values)):
				values[j] = 9
			if i != 0:
				i -= 1
			else:
				i += 1
		else:
			i += 1
	return values

f = open('B-large.in', 'r')
w = open('output.txt', 'w')
nums = f.readlines()
count = 0
for number in nums:
	if count != 0:
		w.write('Case #' + str(count) + ': ')
		number = int(number)
		temp = number
		length = 0
		while temp >= 1:
			temp //= 10
			length += 1
		if length == 1:
			w.write(str(number) + '\n')
		else:
			values = findIntAtPlace(number, length)
			values = findTidyNumber(values)
			values = int(''.join(map(str, values)))
			w.write(str(values) + '\n')
	count += 1