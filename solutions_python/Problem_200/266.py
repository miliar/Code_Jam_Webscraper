t = int(input())
for i in range(1, t + 1):
	nums = list(input())
	n = len(nums)
	j = n - 1
	k = j
	while j > 0:
		if int(nums[j]) >= int(nums[j-1]):
			j -= 1
		else:
			nums[j-1] = str(int(nums[j-1]) - 1)
			nums[j:k+1] = ['9'] * (k+1-j)
			j -= 1
			k = j 
	result = "".join(nums).lstrip('0')
	print("Case #{}: {}".format(i, result))