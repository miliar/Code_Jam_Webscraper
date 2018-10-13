#!/usr/bin/env python3

## Solve Problem ##

def tidyNumbers(n):
	if len(n) is 1:
		return n
	while(len(n) > 1):
		for i in range(0, len(n)):
			if i is len(n)-1:
				return n		
			if n[i] > n[i+1]:
				n = str(int(n) - (int(n[i+1:])+1))
				break
	return n

## Produce output ##

t = int(input())  # reads in number of test cases

# loop for all cases get answer and print it to output
for i in range(1, t + 1):
	print("Case #{}: {} ".format(i, tidyNumbers(input())))
