import sys

def solve(in_file, out_file, case):
	out_file.write('Case #' + str(case + 1) + ': ')
	
	line = in_file.readline().replace('\n', '')
	max_shyness = int(line.split(' ')[0])
	shyness_quantity = line.split(' ')[1]
	
	level = 1
	sum = 0
	largest_diff = 0
	while (level <= (max_shyness + 1)):
		quantity = int(shyness_quantity[level - 1])
		sum += quantity
		if (level - sum) > largest_diff:
			largest_diff = level - sum
		level += 1
	
	out_file.write(str(largest_diff))
	out_file.write('\n')

if len(sys.argv) != 2:
	print 'Please provide one parameter with the name of the input file location relative to this file.'
else:
	in_file = open(str(sys.argv[1]), 'r')
	out_file = open(str(sys.argv[1]).replace('.in', '.out'), 'w')
	cases = int(in_file.readline())
	case = 0
	while (case < cases):
		solve(in_file, out_file, case)
		case += 1
	in_file.close()
	out_file.close()