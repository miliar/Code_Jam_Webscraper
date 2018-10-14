#!/usr/bin/env python3

import re

## Solve Problem ##

def flipPancakes(s, k):
	if '-' not in s:
		return 0

	if k is len(s):
		if '+' not in s:
			return 1
		else:
			return 'IMPOSSIBLE'
	
	if '-'*k in s[:int(len(s)/2)]:
		try:
			flips = 1 + flipPancakes(s.replace('-'*k, '+'*k, 1), k)
		except TypeError:
			flips = 'IMPOSSIBLE'
		return flips

	s = s[::-1]
	if '-'*k in s:
		try:
			flips = 1 + flipPancakes(s.replace('-'*k, '+'*k, 1), k)
			s = s[::-1]
		except TypeError:
			flips = 'IMPOSSIBLE'
		return flips
	s = s[::-1]

	if "-{}-".format('+'*(k-1)) in s:
		try:
			flips = 1 + flipPancakes(s.replace("-{}-".format('+'*(k-1)), "+{}".format('-'*(k)), 1), k)
		except TypeError:
			flips = 'IMPOSSIBLE'
		return flips

	regex = "-.{}{}{}".format('{', k-1, '}')
	if re.search(regex, s):
		pattern = re.search(regex, s)
		newPattern = pattern.group(0)[1:]
		newPattern = newPattern.replace('+', '=')
		newPattern = newPattern.replace('-', '+')
		newPattern = newPattern.replace('=', '-')
		try:
			flips = 1 + flipPancakes(s.replace(pattern.group(0), "+{}".format(newPattern), 1), k)
		except TypeError:
			flips = 'IMPOSSIBLE'
		return flips

	return 'IMPOSSIBLE'

## Produce output ##

t = int(input())  # reads in number of test cases

# loop for all cases get answer and print it to output
for i in range(1, t + 1):
	case = input().split(' ')
	s = case[0]
	k = int(case[1])
	print("Case #{}: {} ".format(i, flipPancakes(s, k)))
