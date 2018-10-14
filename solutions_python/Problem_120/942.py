import math

nCases = int(input())
for casenum in range(nCases):
	str_nums = input().split()
	r = int(str_nums[0])
	t = int(str_nums[1])
	dec_res = 0.25 - (r / 2) + math.sqrt((r/2 - 0.25)**2 + t/2)
	print("Case #{0}: {1}".format(casenum+1, int(dec_res)))