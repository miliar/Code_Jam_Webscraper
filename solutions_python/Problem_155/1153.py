#!/usr/bin/python3

import sys

def ovation(audience):
	needed = 0
	standing = int(audience[0])
	for shyness in range(1, len(audience)):
		if standing < shyness:
			d = shyness - standing
			standing += d
			needed += d
		standing += int(audience[shyness])
	return  needed

if __name__ == '__main__':
	test_count = int(sys.stdin.readline())

	for t in range(1, test_count + 1):
		audience = sys.stdin.readline().split()[1]
		needed = ovation(audience)
		print('Case #%d: %d' % (t, needed))
