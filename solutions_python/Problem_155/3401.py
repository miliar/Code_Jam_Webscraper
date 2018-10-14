import os

def solve(f_in):
	row1_list = f_in.readline().split()
	smax = int(row1_list[0])

	answer = 0
	people_total = 0

	for i in range(smax + 1):
		diff = i - people_total
		if diff > 0:
			answer += diff
			people_total = i
		people_total += int(row1_list[1][i])
	return answer

if __name__ == "__main__":
	input_filename = 'A-large.in'
	output_filename = 'Qualification_ProblemA_Large_Output.txt'

	f_in = open(input_filename)
	counter = 0
	while os.path.isfile(output_filename):
		counter += 1
		output_filename = output_filename.split('.')[0] + str(counter) + '.txt'
	f_out = open(output_filename, 'a')

	test_cases = int(f_in.readline())
	
	for i in range(test_cases):
		ans = solve(f_in)
		f_out.write('Case #' + str(i + 1) +': ' + str(ans) + '\n')

	f_in.close()
	f_out.close()

	print 'Problem completed!'




