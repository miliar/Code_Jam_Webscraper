
input = open("A-large.in", "r")
output = open("A-large.out", "w")


T = int(input.readline().strip())

def flip(k):
	if k == '-':
		return '+'
	else:
		return '-'

for j in range(1, T+1):
	output.write("case #{}: ".format(j))
	input_line = input.readline().strip()
	seq = [k for k in input_line.split()[0]]
	size = int(input_line.split()[1])

	count = 0
	for i in range(len(seq) - size + 1):
		if seq[i] == '-':
			count += 1
			for k in range(size):
				seq[i + k] = flip(seq[i + k])

	if '-' in seq:
		output.write("IMPOSSIBLE")
	else:
		output.write(str(count))
	output.write("\n")


input.close()
output.close()

