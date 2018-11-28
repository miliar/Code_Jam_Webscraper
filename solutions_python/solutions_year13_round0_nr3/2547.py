import math
import sys

def isPalindrome(x):
	palindrome = True
	xstr = str(x)
	for dindex in range(len(xstr)):
		if (xstr[dindex] != xstr[-dindex-1]):
			palindrome = False
	return palindrome


def solve(a,b):
	count = 0

	x = math.sqrt(a)
	xs = int(x * x)
	if (x==int(x)) and isPalindrome(int(x)) and isPalindrome(xs):
		count = 1
		# print 'pal: ', x, xs
	x = int(x) + 1
	xs = x*x
	while (xs <= b):
		if isPalindrome(xs) and isPalindrome(x):
			count += 1
			# print 'pal: ', x, xs
		x = x+1
		xs = x*x

	return count

filename = sys.argv[1]
fin = open(filename, 'r')
#fout = open('p3res.txt', 'w')


cases = int(fin.readline())
for case in range(cases):
	[a, b] = fin.readline().split()
	# print a, b
	print "Case #{}: {}".format(case + 1, solve(int(a), int(b)))
	#fout.write("Case #{}: {}".format(case + 1, solve(int(a), int(b))))

fin.close()
#fout.close()



