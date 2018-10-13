def isTidy(numbers):
	tidy = True
	for x in range(len(numbers)):
		for y in range(len(numbers) - x):
			if numbers[x] > numbers[x + y]:
				tidy = False
				return tidy
	return tidy

def makeTidy(numbers):
	for x in range(len(numbers) - 1):
		if numbers[x] > numbers[x + 1]:
			numbers[x] = numbers[x] - 1
			for y in range(1, len(numbers) - x):
				numbers[x + y] = 9
	#print numbers
	num = int(''.join(map(str,numbers)))
	return num


def getDigits(number):
	numbers = []
	while number != 0:
		numbers.append(number % 10)
		number = number / 10
	return numbers

f_in = open("B-large.in", "r")
f_out = open("tidy_numbers_output", "w")
numTests = int(f_in.readline())
for x in range(numTests):
	number = int(f_in.readline())
	numbers = getDigits(number)
	numbers.reverse()
	while not isTidy(numbers):
		number = makeTidy(numbers)
	f_out.write("Case #" + str(x + 1) + ": " + str(number))
	if x < numTests - 1:
		f_out.write("\n")