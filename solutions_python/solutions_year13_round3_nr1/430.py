import math

vowels = set(['a','e','i','o','u'])

def substring_checker(substring, n):
	l = len(substring)
	longest_run = 0
	curr_run = 0
	for i in range(l):
		if substring[i] in vowels:
			if curr_run > longest_run:
				longest_run = curr_run
			curr_run = 0
		else:
			curr_run += 1
	if curr_run > longest_run:
		longest_run = curr_run
	return True if longest_run >= n else False


def checker(case):
	good_substrings = 0
	name, n = case[0], int(case[1])
	L = len(name)
	for l in range(n, L+1):
		for start in range(0, L-l+1):
			substring = name[start:(start+l)]
			if substring_checker(substring, n):
				good_substrings += 1	
	return good_substrings
	

input_file = open('small_input', 'r')
output_file = open('small_output', 'w')
#input_file = open('large_input', 'r')
#output_file = open('large_output', 'w')
num_cases = int(input_file.readline())
output = ''

for i in range(1, num_cases+1):
	case = input_file.readline().split()
	output += 'Case #{0}: {1}\n'.format(i, checker(case))
output_file.write(output)

output_file.close()
input_file.close()