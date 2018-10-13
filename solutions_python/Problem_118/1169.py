# -*- coding: utf-8 -*-

from collections import deque
import io
import math

def is_square(num):
	sqrt = (int)(math.sqrt(num))
	if num != pow(sqrt, 2):
		return False

	return is_fair(sqrt)

def is_fair(num):
	if num < 10:
		return True

	pipe = deque()
	digit = num
	while digit > 0:
		pipe.append(digit % 10)
		digit = (int)(digit / 10)

	while len(pipe) > 1:
		left = pipe.pop()
		right = pipe.popleft()
		if left != right:
			return False

	return True

def main():
	results = []
	with io.open("C-small-attempt0.in", "r") as f:
		testcase_count = int(f.readline())
		for testcase in range(testcase_count):
			digits = f.readline().split(' ')
			lower = int(digits[0])
			upper = int(digits[1])

			count = 0
			for num in range(lower, upper + 1):
				if is_square(num) and is_fair(num):
					count += 1

			results.append("Case #{0}: {1}".format(testcase + 1, count))

	with io.open("C-small-attempt0.out", "w") as f:
		for i in range(len(results)):
			f.write(results[i])
			if i != len(results) - 1:
				f.write('\n')

if __name__ == "__main__":
	main()
