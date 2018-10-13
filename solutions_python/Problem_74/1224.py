BUTTON_POS = 0
TASK_NUMBER = 1

def testcase(line):
	orange_ops = []
	blue_ops = []
	
	cur_orange = 1
	cur_blue = 1
	
	seconds = 0
	
	params = line.split()
	
	# Get N
	N = int(params[0])
	params = params[1:]
	
	for i in xrange(0, len(params), 2):
		if 'O' == params[i]:
			orange_ops.append((int(params[i + 1]), (i + 1) / 2))
		else:
			blue_ops.append((int(params[i + 1]), (i + 1) / 2))

	while [] != orange_ops and [] != blue_ops:
		if orange_ops[0][TASK_NUMBER] > blue_ops[0][TASK_NUMBER]:
			# Only blue can push, orange & blue can move
			if cur_blue == blue_ops[0][BUTTON_POS]:
				# Blue at spot, blue pushes
				blue_ops = blue_ops[1:]
			else:
				# Blue needs to move to spot
				cur_blue += 1 if blue_ops[0][BUTTON_POS] > cur_blue else -1
			
			# Orange
			if cur_orange == orange_ops[0][BUTTON_POS]:
				# Orange at spot, wait
				pass
			else:
				# Orange needs to move to spot
				cur_orange += 1 if orange_ops[0][BUTTON_POS] > cur_orange else -1
		else:
			# Only orange can push, orange & blue can move
			if cur_orange == orange_ops[0][BUTTON_POS]:
				# Orange at spot, orange pushes
				orange_ops = orange_ops[1:]
			else:
				# Orange needs to move to spot
				cur_orange += 1 if orange_ops[0][BUTTON_POS] > cur_orange else -1
			
			# Blue
			
			if cur_blue == blue_ops[0][BUTTON_POS]:
				# blue at spot, wait
				pass
			else:
				# blue needs to move to spot
				cur_blue += 1 if blue_ops[0][BUTTON_POS] > cur_blue else -1
		seconds += 1
		
	remain_ops = orange_ops if orange_ops != [] else blue_ops
	remain_pos = cur_orange if orange_ops != [] else cur_blue
	
	while [] != remain_ops:
		if remain_pos == remain_ops[0][BUTTON_POS]:
			# Remainer at spot, push
			remain_ops = remain_ops[1:]
		else:
			# Remainer needs to move to spot
			remain_pos += 1 if remain_ops[0][BUTTON_POS] > remain_pos else -1
		seconds += 1
	
	return seconds
	
def main():
	f_in = open('a.in', 'r')
	data = f_in.readlines()
	
	f_out = open('a.out', 'w')
	
	# number of test cases
	T = int(data[0])
	data = data[1:]
	
	for i in xrange(T):
		test_answer = testcase(data[i])
		f_out.write('Case #%d: %d\n' % (i + 1, test_answer))
		f_out.flush()
		
	f_out.close()
	f_in.close()

if __name__ == "__main__":
	main()