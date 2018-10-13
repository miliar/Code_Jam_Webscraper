import sys
import math

def solve(in_file, out_file, case):
	out_file.write('Case #' + str(case + 1) + ': ')
	
	line = in_file.readline().replace('\n', '')
	n = int(line.split(' ')[0])
	k = int(line.split(' ')[1])
	
	stalls = [n]
	
	while(k > 1):
		k -= 1
		max_index = stalls.index(max(stalls))
		if(stalls[max_index] == 1):
			del stalls[max_index]
		else:
			new_split_stalls = split_num(stalls[max_index])
			del stalls[max_index]
			i = len(new_split_stalls) - 1
			while(i >= 0):
				stalls.insert(max_index, new_split_stalls[i])
				i -= 1
	
	max_stall = max(stalls)
	max_stall -= 1
	left = max_stall / 2
	right = max_stall - left
	out_file.write(str(max(left, right)) + " " + str(min(left, right)))
	
	out_file.write('\n')
	
def solve2(in_file, out_file, case):
	out_file.write('Case #' + str(case + 1) + ': ')
	
	line = in_file.readline().replace('\n', '')
	n = int(line.split(' ')[0])
	k = int(line.split(' ')[1])
	
	limit_index = 0
	limit = 1
	
	# biggest space left, left/right spaces open
	# - open, x closed, o just closed
	# 8 --------			8
	# 4 ---o----	3/4		3,4
	# 3 ---x-o--	1/2		3,1,2
	# 2 -o-x-x--	1/1		1,1,1,2
	# 1 -x-x-xo-	0/1		1,1,1,1
	# 1 ox-x-xx-	0/0
	# 1 xxox-xx-	0/0
	# 1 xxxxoxx-	0/0
	# 0 xxxxxxxo	0/0
	
	while(k > 1):
		k -= 1
		if(limit_index == 0):
			n /= 2
			if(n <= 0):
				n = 1
		limit_index += 1
		if(limit_index == limit):
			limit *= 2
			limit_index = 0
	
	stall_index = int(math.ceil(float(n) / 2))
	left = stall_index - 1
	right = n - stall_index
	
	out_file.write(str(max(left, right)) + " " + str(min(left, right)))
	
	out_file.write('\n')

def split_num(num):
	num -= 1
	if(num == 1):
		return [num]
	else:
		return [num / 2, num - (num / 2)]
	
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