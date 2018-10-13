import math
def solve(number):
	num = str(number)
	nums = [int(n) for n in num]
	higher = [0]
	idx = 0

	current = number
	while len(higher) < len(num):
		num = str(current)
		nums = [int(n) for n in num]
		higher = [0]
		for i in range(1, len(nums)):
			if nums[i] > nums[i-1]:
				higher.append(1)
			elif nums[i] == nums[i-1]:
				higher.append(0)
			else:
				if 1 in higher:
					pos = higher[::-1].index(1)
					pos = len(higher) - pos - 1
					current = current - (current % int(math.pow(10, len(num) - pos - 1)) + 1)
				else:
					current = current - (current % int(math.pow(10, len(num) - 1)) + 1)
				break
	return current


with open('large.txt') as f:
	num_cases = int(f.readline())
	for i in range(num_cases):
		number = int(f.readline().strip())
		result = solve(number)
		print "Case #{}: {}".format(i + 1, result)