def epilogue(result, num):
	out_file.write("Case #" + str(num+1) + ": " + result + '\n')

in_file, out_file = open('B-large.in', 'r'), open('B-large.out', 'w')

num_cases = int(in_file.readline())
for case_num in range(num_cases):
	digits = list([int(x) for x in in_file.readline().split()[0]])
	done = False
	while not done:
		done = True
		for i in range(len(digits)-1):
			if digits[i] > digits[i+1]:
				digits[i] -= 1
				for j in range(i+1, len(digits)):
					digits[j] = 9
				done = False
	biggest_tidy = "".join([str(x) for x in digits])
	epilogue(str(int(biggest_tidy)), case_num)