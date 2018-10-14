
import sys


def get_int_array(input_str):
	out = []
	for i in range( len(input_str)):
		out.append(int(input_str[i]))
	return out



def parse_input_file(file_name):
	testcase = {}
	lines = []

	f = open(input1, 'r')
	for line in f:
		lines.append(line)

	num_of_tests = int(lines[0])
	print "num_of_tests:", num_of_tests

	for i in range(1, num_of_tests+1):
		line = lines[i].split()
		case = {}
		case['max_shy'] = int(line[0])
		case['arr'] = get_int_array(line[1])
		case['result'] = 0
		testcase[i] = case
		print testcase[i]
	
	return testcase

def print_result(testcase):
	for key, value in testcase.iteritems():
		print "Case #%s: %d"%(key, value['result'])

def compute(case):
	arr = case['arr']

	total = 0
	need = 0
	all_need = 0
	for i in range(len(arr)):
		if arr[i] == 0:
			continue

		if total < i:
			need = i - total
			print 'need: ', need
			all_need += need
			total += need

		total += arr[i]	

	case['result'] = all_need
		 

def get_result(testcase):
	for k, v in testcase.iteritems():
		compute(v)

def save_file(file_name, testcase):
	f = open(file_name, 'w')
	for key, value in testcase.iteritems():
		f.write("Case #%s: %d\n"%(key, value['result']))	 

if __name__ == '__main__':
	input1 = sys.argv[1]
	output1 = sys.argv[2]
 	testcase = parse_input_file(input1)
 	get_result(testcase)
 	print_result(testcase)
 	save_file(output1, testcase)








