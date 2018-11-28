from sys import stdin
from math import ceil

input = stdin.readlines()
T = int(input[0])

x = 1
nums = []
while x ** 2 <= 10**14:
	if str(x) == str(x)[::-1] and str(x ** 2) == str(x ** 2)[::-1]:
		nums.append(x**2)
	x += 1

for i in range(T):
	line = input[i+1].split()
	A, B = int(line[0]), int(line[1])
	num = 0

	for x in range(len(nums)):
		if A <= nums[x] <= B:
			num += 1

	print "Case #{0}: {1}".format(i+1, num)