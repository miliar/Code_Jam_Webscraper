#!/usr/bin/env python
num_cases = int(raw_input())  # read a line with a single integer

cases = [raw_input() for _ in xrange(num_cases)]

for x, case in enumerate(cases):
	
	nums = [int(num) for num in case]

	i = len(nums) - 1
	cascade_point = len(nums)
	while i > 0:
		if nums[i] < nums[i-1]:
			cascade_point = i
			nums[i-1] -= 1
		else:
			nums[i] = str(nums[i])
		i -= 1

	for i in xrange(cascade_point, len(nums)):
		nums[i] = '9'

	if nums[0] == 0:
		nums.pop(0)
	else:
		nums[0] = str(nums[0])

	print 'Case #{}: {}'.format(x+1, ''.join(nums))
