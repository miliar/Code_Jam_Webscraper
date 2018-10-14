import math

test_cases = raw_input()

def is_square(apositiveint):
	if apositiveint in [0, 1]: return True

	x = apositiveint // 2
	seen = set([x])
	while x * x != apositiveint:
		x = (x + (apositiveint // x)) // 2
		if x in seen: return False
		seen.add(x)
	return True

for i in range(0, int(test_cases)):
	nums = raw_input().split(" ")
	
	count = 0
	for j in range(int(nums[0]), int(nums[1]) + 1):
		if (str(j) == str(j)[::-1] and is_square(j) and str(int(math.sqrt(j)))[::-1] == str(int(math.sqrt(j))) ):
			count += 1
	print "Case #" + str(i+1) +": "+str(count)
