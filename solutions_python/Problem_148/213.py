T = int(raw_input())
for i in xrange(T):
	n, x = raw_input().split()
	n = int(n)
	x = int(x)
	read = raw_input().split()
	nums = [int(ff) for ff in read]

	nums.sort()
	nums.reverse()

	count = 0
	i1 = 0
	i2 = 0

	while len(nums) > 0:
		if len(nums) == 1:
			count += 1
			break
		v = nums[0]
		ind = 1
		while ind < len(nums) and nums[ind] + v > x:
			ind += 1
		if ind == len(nums):
			count += 1
			nums.remove(v)
		else:
			count += 1
			nums.remove(nums[ind])
			nums.remove(v)



	ans = count
	print "Case #" + str(i+1) + ": " + str(ans)
