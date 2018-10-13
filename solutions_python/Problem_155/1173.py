import sys

path_in = sys.argv[1]
path_out = sys.argv[2]

file_in = open(path_in, 'r')
file_out = open(path_out, 'w')

num_tests = int(file_in.readline().strip())
solution = list()

def solve(max_shyness, audience):
	persons_to_add = 0
	persons_clapping = 0
	
	for i in range(0, len(audience)):
		shyness_level = i
		persons = int(audience[i])
		
		if persons_clapping < shyness_level:
			persons_needed = shyness_level - persons_clapping
			persons_to_add += persons_needed
			persons_clapping += persons_needed
		
		persons_clapping += persons

	return persons_to_add

def run():
	for i in range(0, num_tests):
		test_case = file_in.readline().strip()
		max_shyness, audience = test_case.split(' ')
		solution.append('Case #{}: {}\n'.format(i+1, solve(max_shyness, audience)))

run()

file_out.writelines(solution)
file_out.flush()

file_in.close()
file_out.close()