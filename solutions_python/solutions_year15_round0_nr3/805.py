import sys

quaternions = {
	'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k', '-1': '-1', '-i': '-i', '-j': '-j', '-k': '-k'},
	'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j', '-1': '-i', '-i': '1', '-j': '-k', '-k': 'j'},
	'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i', '-1': '-j', '-i': 'k', '-j': '1', '-k': '-i'},
	'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1', '-1': '-k', '-i': '-j', '-j': 'i', '-k': '1'},
	'-1': {'1': '-1', 'i': '-i', 'j': '-j', 'k': '-k', '-1': '1', '-i': 'i', '-j': 'j', '-k': 'k'},
	'-i': {'1': '-i', 'i': '1', 'j': '-k', 'k': 'j', '-1': 'i', '-i': '-1', '-j': 'k', '-k': '-j'},
	'-j': {'1': '-j', 'i': 'k', 'j': '1', 'k': '-i', '-1': 'j', '-i': '-k', '-j': '-1', '-k': 'i'},
	'-k': {'1': '-k', 'i': '-j', 'j': 'i', 'k': '1', '-1': 'k', '-i': 'j', '-j': '-i', '-k': '-1'}
}

def solve(string):
	target = 'kji'
	current = '1'
	while len(string) > 0:
		current = quaternions[string[0]][current]
		string = string[1:]

		if target.startswith(current):
			target = target[1:]
			current = '1'
			if len(target) == 0 and len(string) == 0:
				return True
			elif len(target) == 0:
				target = target + 'i'
				current = 'i'
	return False

def run():
	for i in range(0, num_tests):
		length, count = file_in.readline().strip().split(' ')
		length = int(length)
		count = int(count)
		string = count * file_in.readline().strip()
		solution.append('Case #{}: {}\n'.format(i+1, 'YES' if solve(string[::-1]) else 'NO'))

if __name__ == '__main__':
	path_in = sys.argv[1]
	path_out = sys.argv[2]

	file_in = open(path_in, 'r')
	file_out = open(path_out, 'w')

	num_tests = int(file_in.readline().strip())
	solution = list()

	run()

	file_out.writelines(solution)
	file_out.flush()

	file_in.close()
	file_out.close()
