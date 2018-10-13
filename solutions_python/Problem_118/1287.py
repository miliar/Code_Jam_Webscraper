import re
import sys
import math

def isPalindrome(n):
	if str(int(n)) == str(int(n))[::-1]:
		return True
	return False

f = open(sys.argv[1], "r")
n = int(f.readline())
for i in range(1,n+1):
	sys.stdout.write("Case #" + repr(i) + ": ")
	match = re.search("(\d+) (\d+)", f.readline())
	start, end = int(match.group(1)), int(match.group(2))
	count = 0
	for j in range(start, end+1):
		s = math.sqrt(j)
		if (s % 1 > .0001):
			continue
		if isPalindrome(j) and isPalindrome(s+.1):
			count += 1
	sys.stdout.write(repr(count) + "\n")