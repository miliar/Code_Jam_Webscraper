import sys

input_file = sys.stdin
output_file = sys.stdout

t = int(input_file.readline().strip())

for i in range(t):
	n = int(input_file.readline().strip())
	line = input_file.readline().split()

	bits = []
	for j in range(32):
		bits.append(False)


	min_number = -1
	s = 0
	for j in range(n):
		number = int(line[j])
		s += number
		if ((-1 == min_number) or (number < min_number)):
			min_number = number
		
		k = 0
		while number > 0:
			if number % 2 != 0:
				bits[k] = not(bits[k])
			k += 1
			number /= 2

	possible = True
	for j in range(32):
		if bits[j]:
			possible = False
			break

	output_file.write("Case #" + str(i + 1) + ": ")
	if possible:
		output_file.write(str(s - min_number))
	else:
		output_file.write("NO")
	output_file.write("\n")

