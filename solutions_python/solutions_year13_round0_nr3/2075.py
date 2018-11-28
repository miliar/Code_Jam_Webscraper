# Fair and Square number finder
from math import sqrt

def ParseInput(f):
	amt = int(f.readline())
	intervals = []
	for line in f.readlines():
		intervals.append([ int(a) for a in line.strip('\n').split(' ') ])
	return intervals

def IsPalindrome(num):
	s = str(num)
	return s == s[::-1]


if __name__ == '__main__':
	path = raw_input("File: ")
	cases = None
	with open(path, 'r') as infile:
		cases = ParseInput(infile)

	with open('./outfile', 'w') as outfile:
		casenum = 1
		for case in cases:
			# Iterate over each defined interval
			count = 0
			for i in range(case[0],case[1]+1):
				# Now, check for palindrome, square, and square root palindrome
				root = sqrt(i)
				if root % 1 == 0:
					if IsPalindrome(i):
						if IsPalindrome(int(root)):
							count += 1
			outfile.write("Case #%r: %r\n" % (casenum, count))
			casenum += 1

