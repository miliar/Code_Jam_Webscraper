# find a pattern
import heapq
t = int(input())
for i in range(1, t + 1):
	nums = input().split(" ")
	n = int(nums[0])
	k = int(nums[1])
	exp = 0
	copy = k
	while copy > 0:
		exp += 1
		copy //= 2
	if n == k:
		print("Case #{}: {} {}".format(i, 0, 0))
	else:
		print("Case #{}: {} {}".format(i, (n-k+2**(exp-1))>>exp, (n-k)>>exp))