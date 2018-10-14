'''
	problem

	
'''
import sys

def tidy(n):
	digits = map(lambda x:int(x),list(str(n)))
	di = len(digits) - 1
	for dj in list(reversed(range(0,len(digits)-1))):
		if( digits[dj] > digits[di]):
			return False, dj + 1
		di = di - 1
	return True, 0

def problem(n):
	while ( n > 0):
		is_tidy, violating_index = tidy(n)
		if(is_tidy):
			return n
		else:
			n = n - 1



def main():
	input_file = sys.argv[1]
	with open(input_file) as i:
		cases = map(lambda x:x.rstrip(), i.readlines())

	num_cases = cases[0]
	cases = cases[1:]

	output_file = sys.argv[1].split('.')[0] + '.out'
	o = open(output_file,'w+')

	case_num = 1
	for case in cases:
		result = problem(int(case))
		o.write("Case #" + str(case_num) + ": " + str(result) + "\n")
		case_num += 1
	o.close()


if(__name__ == "__main__"):
	main()


