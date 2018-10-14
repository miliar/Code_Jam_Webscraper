input_file = open('B-small-attempt1.in','r')
num_inputs = input_file.readline()

output = open('output.out', 'a')

def is_tidy(string):
	if len(string) == 1:
		return True
	for i in range(len(string)):
		if i > 0 and string[i-1] > string[i]:
			return False
	return True

def tidy_until_index(string):
	if len(string) == 1:
		return 0
	for i in range(len(string)):
		if i > 0 and string[i-1] >= string[i]:
			return i - 1
	return len(string)

item = 1

for i in range(int(num_inputs)):
	input = input_file.readline().strip()
	answer = ''
	if is_tidy(input):
		answer = 'Case #' + str(item) + ': '+ input
	else:
		inputInt = int(input)
		index = tidy_until_index(input)
		exponent = len(input) - index - 1;
		# print('exponent', exponent)
		divisor = 10 ** exponent
		# print('divisor', divisor)
		remainder = int(input) % divisor
		if remainder == 0:
			answer = inputInt - 1
			answer = 'Case #' + str(item) + ': '+ str(answer)
		else:
			answer = inputInt - remainder - 1
			answer = 'Case #' + str(item) + ': ' + str(answer)
	item = item + 1
	output.write(answer+'\n')