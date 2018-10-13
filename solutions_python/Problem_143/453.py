import sys

input_file = 'A-small-attempt0.in'
output_file = 'A-small.out'

def run(resolve):
	oldstdin = sys.stdin
	fi = open(input_file, 'r')
	fo = open(output_file, 'w')
	sys.stdin = fi
	fo.write(process_cases(resolve))
	sys.stdin = oldstdin

def process_cases(resolve):
	case_total_num = int(input())
	result = ''
	for i in range(case_total_num):
		res = 'Case #%d: %s' % (i + 1, resolve(i+1))
		print(res)
		result = '%s%s\n' % (result, res)
	return result

def resolve(case_num):
	return case_num

if __name__ == '__main__':
	run(resolve)
		