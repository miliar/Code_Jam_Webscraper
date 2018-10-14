import os
import copy

def solve(f_in):
	n = int(f_in.readline())
	N_array = sorted([float(elem) for elem in f_in.readline().split()])
	K_array = sorted([float(elem) for elem in f_in.readline().split()])	

	merged = merge(N_array, K_array)

	war_optimal = find_war_optimal(merged)
	deceit_optimal = find_deceit_optimal(merged)
	return ' '.join([str(deceit_optimal), str(war_optimal)])

def find_war_optimal(merged_war):
	ans = 0
	N_counter = 0
	for elem in merged_war:
		if elem == 'N':
			N_counter += 1
		else:
			if N_counter == 0:
				ans += 1
			else:
				N_counter -= 1
	return ans

def find_deceit_optimal(merged_deceit):
	ans = 0
	K_counter = 0
	for elem in merged_deceit:
		if elem == 'K':
			K_counter += 1
		else:
			if K_counter > 0:
				K_counter -= 1
				ans += 1
	return ans



def merge(N_array, K_array):
	output = []
	n = len(N_array)
	i = 0
	j = 0
	while (i < n or j < n):
		if i >= n:
			N_value = 2
		else:
			N_value = N_array[i]
		if j >= n:
			K_value = 2
		else:
			K_value = K_array[j]
		if N_value < K_value:
			output.append('N')
			i += 1
		else:
			output.append('K')
			j += 1
	return output

if __name__ == "__main__":
	input_filename = 'D-large.in'
	output_filename = 'Qualification_ProblemC_large_0.txt'

	f_in = open(input_filename)
	counter = int(output_filename.split('.')[0][-1])
	while os.path.isfile(output_filename):
		counter += 1
		output_filename = output_filename.split(str(counter - 1) + '.')[0] + str(counter) + '.txt'
	f_out = open(output_filename, 'a')

	test_cases = int(f_in.readline())
	
	for i in range(test_cases):
		ans = solve(f_in)
		f_out.write('Case #' + str(i + 1) +': ' + str(ans) + '\n')

	f_in.close()
	f_out.close()

	print 'Problem completed!'