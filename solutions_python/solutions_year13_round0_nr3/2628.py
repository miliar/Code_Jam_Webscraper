import math
def is_palindrome(num):
	num = str(num)
	for i in xrange(len(num)/2 + 1):
		if not num[i] == num[-1-i]:
			return False
	return True

def get_fair_squares(lower,higher,case_num):
	res_cnt = 0
	for num in xrange(lower,higher+1):
		if is_palindrome(num):
			sqRoot = int(math.sqrt(num))
			if sqRoot * sqRoot == num and is_palindrome(sqRoot):
				res_cnt += 1
	print 'Case #' + str(case_num) + ':' ,res_cnt

def parse_input():
	ranges = []
	fname = 'fair_square.in'
	inFile =  open(fname, 'r')
	size = int(inFile.readline())
	for i in xrange(size):
		range_str = inFile.readline().split(' ')
		ranges.append((int(range_str[0]),int(range_str[1])))
	return ranges


for i,pair in enumerate(parse_input()):
	lower,higher = pair
	get_fair_squares(lower,higher,i+1)











