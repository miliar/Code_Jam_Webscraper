import sys
import math
def read_input():
	'''
	Returns a list of test_cases, each of which has:
		[N, S, p, [result1, result2, ...]]
	'''	
	data = sys.stdin.readlines()
	#print data
	test_cases = []
	for test_case in data[1:]:
		line_splitted = test_case.split()
		test_cases.append([int(line_splitted[0]), int(line_splitted[1])])
	return test_cases

def find_num_of_pairs(a, b):
	pairs = set()
	#digits = int(math.log10(b))+1
	
	for num in xrange(a, b+1):
		moved_num = str(num)
		for _ in xrange(len(moved_num)):
			moved_num = moved_num[-1]+moved_num[:-1]
			int_moved_num = int(moved_num)
			if moved_num[0] != 0 and int_moved_num > num and b >= int_moved_num:
				pairs.add((num, moved_num))
	
	#print '[find_num_of_pairs(a, b)]:', a, b, pairs
	return len(pairs)

test_cases = read_input()
#print "test_cases:", test_cases

for ind, test_case in enumerate(test_cases):
	num_of_pairs = find_num_of_pairs(test_case[0], test_case[1])
	print "Case #"+str(ind+1)+": "+str(num_of_pairs)
