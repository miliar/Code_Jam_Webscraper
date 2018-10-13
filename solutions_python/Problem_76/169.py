from operator import itemgetter, attrgetter

def solve(nums):
	checksum = reduce(lambda x,y: x^y, nums)
	if checksum:
		return "NO"	
	total = sum(nums)
	return total - min(nums)
	'''
	lengths = set(map(lambda x: len(bin(x)), sorted(nums, reverse=True)))
	print lengths
	#bin_nums = map(lambda x: bin(x)[2:], sorted(nums, reverse=True))
	len_dict = dict(
									[(length - 2, [bin(num)[2:] for num in nums if len(bin(num)) == length]) for length in lengths]
						)
	print len_dict
#	l = len(bin_nums[0])
#	fd = bin_nums[0][0]
#	while True:
	'''	
	
	
T = int(raw_input())
for case in xrange(1, T + 1):
	N = int(raw_input())
	nums = [int(num) for num in raw_input().split()]
	ans = solve(nums)
	print "Case #%d: %s" % (case, ans)