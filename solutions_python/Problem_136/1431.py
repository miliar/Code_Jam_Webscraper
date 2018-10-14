import math
file = open('B-large.in', 'r')
test_count = int(file.readline().rstrip('\n'))

# TODO: change this later
line_array = []
line = file.readline()
while line != '':
	line_array.append(line.rstrip('\n'))
	line = file.readline()
file.close()

output_file = open('p2-large-output.txt', 'w+')

cookie_count = 0
def get_min(f, c, x):
	# min = x * 1.0 / 2
	# sum = x * 1.0 / 2
	# i = 0
	# while (x - i * c > 0)	:
	# 	sum - (x * 1.0 / (2 + f * i))
	# 	i += 1
	largest_i = (f * x * 1.0 / c - 2) / (f) - 1
	largest_i = int(max(0, math.ceil(largest_i)))
	sum = x * 1.0 / (2 + f * largest_i)
	for i in xrange(largest_i):
		sum += c * 1.0 / (2 + f * i)
	return sum

for i in xrange(test_count):
	row = line_array[i].split()
	c = float(row[0])
	f = float(row[1])
	x = float(row[2])
	string_solution = 'Case #' + str((i + 1)) + ': ' + str(get_min(f, c, x)) + "\n"
	output_file.write(string_solution)

output_file.close()
