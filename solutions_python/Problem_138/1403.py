import math
file = open('D-large.in', 'r')
test_count = int(file.readline().rstrip('\n'))

# TODO: change this later
line_array = []
line = file.readline()
while line != '':
	line_array.append(line.rstrip('\n'))
	line = file.readline()
file.close()

output_file = open('p4-large-output.txt', 'w+')

def play_war(naomi, ken, number_of_bags):
	i = number_of_bags - 1
	ken_counter = number_of_bags - 1
	score = 0
	while i >= 0:
		if (naomi[i] > ken[ken_counter]):
			score += 1
		else:
			ken_counter -= 1
		i -= 1
	return score

def play_dwar(naomi, ken, number_of_bags):
	ken_counter = 0
	score = 0
	for i in range(number_of_bags):
		if naomi[i] > ken[ken_counter]:
			score += 1
			ken_counter += 1
	return score


for i in xrange(test_count):
	number_of_bags = int(line_array[i * 3])
	naomi = line_array[i * 3 + 1].split()
	ken = line_array[i * 3 + 2].split()
	for j in range(number_of_bags):
		naomi[j] = float(naomi[j])
		ken[j] = float(ken[j])
	naomi = sorted(naomi)
	ken = sorted(ken)
	string_solution = 'Case #' + str((i + 1)) + ': ' + str(play_dwar(naomi, ken, number_of_bags)) + ' ' + \
													   str(play_war(naomi, ken, number_of_bags)) + '\n'
	output_file.write(string_solution)

output_file.close()
