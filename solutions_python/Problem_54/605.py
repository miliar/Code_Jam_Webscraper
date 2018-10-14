import sys
import fractions

def convert(x):
	return long(x)

ll = 0
for line in sys.stdin:
	ll += 1
	if ll == 1:
		continue

	nums = line.rstrip().split(' ')
	nums.pop(0)
	nums = map(convert, nums)
	nums.sort()

	diff = []
	for i in range(len(nums) - 1):
		diff.append(nums[i + 1] - nums[i])

	m = reduce(fractions.gcd, diff)

	ret = (m - (nums[0] % m)) % m
	print "".join(("Case #", str(ll - 1), ": ", str(ret)))

