import sys


def solve(s_list):

	stands = 0
	guests = 0

	for i in range(len(s_list)):

		if i > stands:
			guests += (i - stands)
			stands += (i - stands)

		stands += s_list[i]

	return guests



num_cases = sys.stdin.readline()
num_cases = int(num_cases)

for i in range(1, num_cases + 1):
	line = sys.stdin.readline()
	
	_, s_str = line.split()
	s_list = map(int, s_str)

	answer = solve(s_list)
	print 'Case #%d: %d' % (i, answer)