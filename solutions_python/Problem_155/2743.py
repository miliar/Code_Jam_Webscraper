#!/usr/bin/env python

from sys import stdin

def solve(maxS, audience):
	levels = {}
	i = 0
	while i < len(audience):
		levels[i] = int(audience[i])
		i += 1

	standing = 0
	friends = 0

	i = 0
	while i < len(audience):

		people = levels[i]
		if people != 0:
			if i - standing > 0: #invite friends
				friends += i - standing
				standing += (i - standing) + people
			else:
				standing += people	

		i += 1

	return friends	

if __name__ == '__main__':
	T = int(stdin.readline())

	for i in range(0,T):
		items = stdin.readline().rstrip("\n").split(" ")
		print "Case #{}: {}".format(i+1, solve(int(items[0]), items[1]))
