import math
import sys

def is_palindrome(n):
	result = False
	n = str(n)
	if n == n[::-1]:
		result = True
	return result

def init():
	lines = []
	for line in sys.stdin:
		lines.append(line.strip())
	t = int(lines[0])
	k = 1
	for i in range(t):
		ranges = lines[k].split()
		a = int(ranges[0])
		b = int(ranges[1])
		result = 0
		for j in range(a, b + 1):
			if is_palindrome(j):
				rooted = int(math.sqrt(j))
				if rooted**2 == j and is_palindrome(rooted):
					result += 1
		k += 1
		print 'Case #' + str(i + 1) + ': ' + str(result)

if __name__ == '__main__':
	init()