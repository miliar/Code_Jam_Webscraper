from math import ceil

cases = int(input())

for casenum in range(1, cases+1):
	N, P = tuple([int(x) for x in input().split()])
	Gs = [int(x)%P for x in input().split()]

	nums = [0]*P
	for G in Gs:
		nums[G] += 1

	res = nums[0]

	if P == 2:
		res += int(ceil(nums[1]/2))
	elif P == 3:
		mins = min(nums[1], nums[2])
		maxs = max(nums[1], nums[2])
		res += mins
		left = max(nums[1], nums[2]) - mins
		res += int(ceil(left/3))

	print("Case #", casenum, ": ", res, sep="")