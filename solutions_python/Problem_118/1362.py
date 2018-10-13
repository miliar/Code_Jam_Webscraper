from math import floor, ceil, sqrt
from ucb import interact
f = open('sqpalin.in')
num_tests = int(f.readline())
test_number = 0

def isPalindrome(num):
	num = str(num)
	for i in range(len(num) // 2):
		if num[i] != num[len(num) -1 -i]:
			return False
	return True

for i in range(num_tests):
	test_number += 1
	total = 0
	cards = []
	bottop = f.readline().split()
	bottom = int(bottop[0])
	top = int(bottop[1])

	'''start at ceil of sqrt of the bottom, end at floor of sqrt of top'''
	start = ceil(sqrt(bottom))
	end = floor(sqrt(top))

	t = start

	while t <= end:
		if isPalindrome(t) and isPalindrome(t*t):
			#interact()
			total += 1
		t += 1

	print("Case #{0}: {1}".format(test_number, total))