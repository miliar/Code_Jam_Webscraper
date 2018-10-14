# Author: Davin Choo
# Email: cxjdavin@gmail.com

# Approach:
# 2) Method 1: Sum up every decrease in value
# 3) Method 2: Run through once to find largest decrease in value.
#			   That is the minimum rate of eating per 10sec
# 			   Run through again to see how much she eats (may be < rate)

T = int(raw_input())

for i in xrange(0, T):
	N = int(raw_input())
	method1 = 0
	method2 = 0

	temp = raw_input().split()
	mushrooms = []
	for j in xrange(0, N):
		mushrooms.append(int(temp[j]))

	max_decrease = 0
	for j in xrange(0, N-1):
		diff = mushrooms[j+1] - mushrooms[j]
		if diff < 0:
			method1 += diff * -1
			if diff < max_decrease:
				max_decrease = diff

	rate = max_decrease * -1
	for j in xrange(0, N-1):
		method2 += min(rate, mushrooms[j])



	output = "Case #" + str(i+1) + ": " + str(method1) + " " + str(method2)
	print output