import math
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
	n = raw_input()
	nums = [int(x) for x in list(n)]
	for j in xrange(len(nums) - 1):
		if nums[len(nums) - 2 - j] > nums[len(nums) - 1 - j]:
			nums[len(nums) - 2 - j] -= 1 
			if nums[len(nums) - 2 - j] == -1:
				nums[len(nums) - 3 - j] -= 1
				nums[len(nums) - 2 - j] = 9 
			for k in xrange(len(nums) - 1 - j, len(nums)):
				nums[k] = 9
	nums = [str(x) for x in nums]
	ans = int("".join(nums))
  	print "Case #{}: {}".format(i, ans)