import math

file_strings = []
with open("tidy_input.txt") as data_file:
	for line in data_file:
		file_strings.append(line.strip())

T = file_strings[0] # number of testcases
file_strings.pop(0)
T = int(T)

for i in range(1, T + 1):
	N = file_strings.pop(0)
	digits = len(N)
	N = int(N)

	max_num = int('1' * digits) # the number we will constantly add to and print eventually
	# If N is smaller than the smallest tidy number of that length, then answer is 9...9
	if max_num > N:
		max_num = ('9' * (digits - 1))

	if len(str(max_num)) == digits:
		while digits > 0:
			while (max_num + int('1' * digits) <= N) and (int(str(max_num)[len(str(N)) - 1]) < 9) :
				max_num = max_num + int('1' * digits)
			digits -= 1

	print("Case #{}: {}".format(i, max_num))
