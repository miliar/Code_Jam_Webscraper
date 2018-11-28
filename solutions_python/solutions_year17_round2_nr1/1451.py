#!/usr/bin/env python3

## Solve Problem ##
def solution(d, n):
	max_t = 0
	while n > 0:
		h = input().split()
		t = (d-int(h[0]))/int(h[1])
		if t > max_t:
			max_t = t
		n -= 1
	return round(d/max_t,6)

## Produce output ##

t = int(input())  # reads in number of test cases

# loop for all cases get answer and print it to output
for i in range(1, t + 1):
	args = input().split()
	print("Case #{}: {}".format(i, solution(int(args[0]),int(args[1]))))
