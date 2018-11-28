import sys
from datetime import datetime

def main(argv):
	start_time = datetime.now()
	filename = argv[1]
	output = argv[2]
	with open(filename) as infile:
		num_tests = int(infile.readline())
		with open(output, 'w+') as out:
			for test_num in range(num_tests):
				out.write('Case #{}: '.format(test_num + 1))
				line = infile.readline().split()
				c = float(line[0])
				f = float(line[1])
				x = float(line[2])
				curr_time = 0
				curr_rate = 2
				while ((x - c)/curr_rate > x/(curr_rate + f)):
					curr_time += c/curr_rate
					curr_rate += f
				curr_time += x/curr_rate
				out.write('{0:.7f}\n'.format(curr_time))

main(sys.argv)