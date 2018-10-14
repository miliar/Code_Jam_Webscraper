import sys

def find_largest_min_dimension(number):
	x = number
	y = 1
	largest_min = 1
	while(x > 0):
		if(min(x, y) > largest_min):
			largest_min = min(x, y)
		x -= 1
		y += 1
	return largest_min

def find_winner(x, r, c):
	# Check for divisibility
	if ((r * c) % x != 0):
		return 'RICHARD'
	# Check for impossible island starting ominos
	if (r >= 7):
		return 'RICHARD'
	# Check for straight longer than max dimension
	if (x > max(r, c)):
		return 'RICHARD'
	largest_min = find_largest_min_dimension(x)
	# Check for smallest dimension of L piece longer than min dimension
	if (largest_min > min(r, c)):
		return 'RICHARD'
	# Check for forced pockets
	if (x >= (2 * min(r, c)) and x >= 4):
		if (largest_min >= r or largest_min >= c):
			return 'RICHARD'
	return 'GABRIEL'

def solve(in_file, out_file, case):
	out_file.write('Case #' + str(case + 1) + ': ')
	
	line = in_file.readline().replace('\n', '')
	x, r, c = line.split(' ')
	x = int(x)
	r = int(r)
	c = int(c)
	winner = find_winner(x, r, c)
	
	out_file.write(winner)
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