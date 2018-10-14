from math import ceil

def problem():
	cases = int(raw_input())
	
	for i in xrange(cases):
		case(i + 1)

def case(i):
	nums = [int(x) for x in raw_input().split(' ')]
	
	N, S, p = nums[:3]
	
	nums = reversed(sorted(nums[3:]))
	nums = filter(lambda x: ceil(x/float(3)) < p, nums)
	
	res = N - len(nums)
	
	for num in nums:
		if not S:
			break
		
		if num % 3 == 1 or num < 2 or num > 28:
			continue
		
		if ceil(num/float(3)) + 1 < p:
			continue
		
		S -= 1
		res += 1	
	
	print 'Case #%d: %d' % (i, res)

if __name__ == '__main__':
	problem()
