filename = 'A-large'

in_file = open(filename + '.in', 'r')
num_test_cases = int(in_file.readline())
test_cases = []

for i in xrange(num_test_cases):
	curr_D, curr_H = [int(x) for x in in_file.readline().split()]
	H_data = []	
	for j in xrange(curr_H):
		H_data.append([int(x) for x in in_file.readline().split()])
	test_cases.append([curr_D, curr_H, H_data])

shortest_times = []
for i in xrange(num_test_cases):
	shortest_time = (float(test_cases[i][0]) - float(test_cases[i][2][0][0])) / float(test_cases[i][2][0][1])
	for j in xrange(test_cases[i][1]):
		s = (float(test_cases[i][0]) - float(test_cases[i][2][j][0])) / float(test_cases[i][2][j][1])
		if s > shortest_time:
			shortest_time = s
	#shortest_times.append(shortest_time)
	shortest_times.append(test_cases[i][0] / shortest_time)


out_file = open(filename + '.out', 'w')

for i in xrange(num_test_cases):
	out_file.write('Case #' + str(i+1) + ': ' + str(shortest_times[i]) + '\n')

out_file.close()
